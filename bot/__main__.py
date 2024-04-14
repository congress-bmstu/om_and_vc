import logging

from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.utils.formatting import Bold, Text

from bot.keyboard import make_row_keyboard
from bot.bot_tasks import toc, get_task, get_format_message, process_by_template, get_task_name

API_TOKEN = '7093022184:AAE3DPPgfgafAdo9J87lLgFbPKUKdVkyoYE'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()


class Form(StatesGroup):
    began = State()
    select_task = State()
    confirm_and_process = State()


async def save_message(message, state):
    user_data = await state.get_data()
    try:
        user_data['messages'].append(message)
    except:
        user_data['messages'] = [message]
    await state.set_data(user_data)


async def delete_last_message(state):
    user_data = await state.get_data()
    try:
        last_message = user_data['messages'].pop()
        await last_message.delete()
    except:
        pass
    else:
        await state.set_data(user_data)


async def delete_all_messages(state):
    user_data = await state.get_data()
    try:
        while len(user_data['messages']) > 0:
            last_message = user_data['messages'].pop()
            await last_message.delete()
    except:
        pass
    else:
        await state.set_data(user_data)


@router.message(Command('stop'))
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply('Состояние бота сброшено')


@router.message(Command('start'))
async def sendhelp(message: types.Message):
    await message.answer('Пиши /solve чтобы начать решать')


@router.message(Command('solve'))
async def solve(message: types.Message, state: FSMContext):
    toc_message = await message.answer(f'Выбери задачу\n{toc}')
    await save_message(toc_message, state)
    await state.set_state(Form.began.state)


def make_bold_examples(text):
    res = []
    for line in text.split('\n'):
        l, r = line.split('//')
        res += [Bold(l), f' //{r}\n']
    return res


@router.message(Form.began)
async def select_task(message: types.Message, state: FSMContext):
    try:
        task_index = message.text.strip().replace(',', '.')
        selected_task = get_task(task_index)
        input_format = get_format_message(selected_task)
    except:
        await delete_last_message(state)
        m1 = await message.answer(
            f'Что-то пошло не так при выборе задания. Я получил на вход `{message.text.strip()}` и сломался.\nПопробуй заново.')
        await save_message(m1, state)
        await solve(message, state)
    else:
        user_data = await state.get_data()
        user_data['selected_task'] = selected_task
        await state.set_data(user_data)

        await delete_all_messages(state)
        m1 = await message.answer(**Text(
            f'Ты выбрал(а) задачу {get_task_name(task_index)}.\nОтправь входные данные в следующем формате \n(только',
            Bold(' жирный '),
            'текст):').as_kwargs()
                                  )
        m2 = await message.answer(**Text(Bold('пример'),
                                         ' //описание формата; смысл в задаче\n',
                                         *make_bold_examples(input_format)).as_kwargs()
                                  )
        await save_message(m1, state)
        await save_message(m2, state)
        await state.set_state(Form.select_task.state)


@router.message(Form.select_task)
async def get_input(message: types.Message, state: FSMContext):
    task_input = message.text

    user_data = await state.get_data()
    user_data['task_input'] = task_input
    await state.set_data(user_data)

    await delete_last_message(state)
    await delete_last_message(state)
    m1 = await message.answer(
        f'Бот получил такие входные данные:\n{task_input}\nПроверь правильность ввода. Продолжить?',
        reply_markup=make_row_keyboard(['Да', 'Нет']))
    await save_message(m1, state)
    await state.set_state(Form.confirm_and_process.state)


@router.message(Form.confirm_and_process)
async def confirm_and_process(message: types.Message, state: FSMContext):
    proceed = message.text == 'Да'
    if proceed:
        await delete_last_message(state)
        await delete_last_message(state)
        user_data = await state.get_data()
        selected_task = user_data['selected_task']

        task_input = user_data['task_input']
        template = selected_task['input_format']
        function = selected_task['function']

        try:
            output, retval = process_by_template(task_input, template, function)
        except Exception as e:
            await message.answer(f'Ошибка выполнения\n{e}', reply_markup=None)
        else:
            await message.answer(f'**Вывод функции:**\n{output}\n**Возвращенное значение:**\n{retval}',
                                 reply_markup=None)
            await state.clear()
    else:
        await delete_last_message(state)
        m1 = await message.answer('Введи новые входные данные:', reply_markup=None)
        await save_message(m1, state)

        user_data = await state.get_data()
        input_format = get_format_message(user_data['selected_task'])
        m2 = await message.answer(f'Формат:\n{input_format}', reply_markup=None)
        await save_message(m2, state)
        await state.set_state(Form.select_task.state)


@router.message()
async def unknown(message: types.Message):
    await message.answer('Не понял тебя, напиши /solve')


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
