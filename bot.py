import logging
import os

from aiogram import Bot, Dispatcher, types, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from keyboard import make_row_keyboard

from bot_tasks import toc, get_task, get_format_message, process_by_template

API_TOKEN = '7093022184:AAE3DPPgfgafAdo9J87lLgFbPKUKdVkyoYE'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
router = Router()
user_preset = {}
user_frame = {}
user_radius = {}

class Form(StatesGroup):
    began = State()
    select_task = State()
    confirm_and_process = State()


@router.message(Command('start'))
async def sendhelp(message: types.Message):
    await message.answer('send /solve')

@router.message(Command('solve'))
async def solve(message: types.Message, state: FSMContext):
    await message.answer(f'select task\n{toc}')
    await state.set_state(Form.began.state)

@router.message(Form.began)
async def select_task(message: types.Message, state: FSMContext):
    selected_task = get_task(message.text.strip())
    input_format = get_format_message(selected_task)
    
    user_data = await state.get_data()
    user_data['selected_task'] = selected_task
    await state.set_data(user_data)
    
    await message.answer(f'you have seleted task {message.text.strip()}.\ngive input in following format')
    await message.answer(input_format)
    await state.set_state(Form.select_task.state)

@router.message(Form.select_task)
async def get_input(message: types.Message, state: FSMContext):
    task_input = message.text
    
    user_data = await state.get_data()
    user_data['task_input'] = task_input
    await state.set_data(user_data)
    
    await message.answer(f'you have provided the following input:\n{task_input}.\ncheck that everything is correct. procceed?', reply_markup=make_row_keyboard(['Yes', 'No']))
    await state.set_state(Form.confirm_and_process.state)

@router.message(Form.confirm_and_process)
async def confirm_and_process(message: types.Message, state: FSMContext):
    proceed = message.text == 'Yes'
    if proceed:
        user_data = await state.get_data()
        selected_task = user_data['selected_task']
        
        task_input = user_data['task_input']
        template = selected_task['input_format']
        function = selected_task['function']
        
        result = process_by_template(task_input, template, function)
        await message.answer('confirm_and_process'+str(result), reply_markup=None)
        await state.clear()
    else:
        await message.answer('rejected', reply_markup=None)

@router.message(Command('drawmap'))
async def draw_map(message: types.Message, state: FSMContext):
    await state.set_state(Form.began.state)
    await message.reply("Выберите пресет", reply_markup=make_row_keyboard(themes))


@router.message(Command('stop'))
async def stop(message: types.Message, state: FSMContext):
    await state.clear()
    await message.reply('состояние бота сброшено')

@router.message()
async def unknown(message: types.Message):
    await message.answer('/solve')

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
