from io import StringIO
import sys

from bot.user_input import ArgumentInput, InputType
from bot.task_list import tasks


def process_by_template(user_input: str, template: list[ArgumentInput | InputType], function):
    try:
        args = [token(line) for line, token in zip(user_input.split('\n'), template)]
    except:
        raise ValueError('Не смог распознать что ты ввёл')

    sys.stdout = my = StringIO()
    retval = function(*args)
    sys.stdout = sys.__stdout__

    return my.getvalue(), retval


def get_table_of_contents():
    i = 1
    toc = ''
    for key in tasks.keys():
        toc += f'{i}. {key}\n'
        j = 1
        for subkey in tasks[key].keys():
            toc += f'  {i}.{j}. {subkey}\n'
            j += 1
        i += 1
    return toc


toc = get_table_of_contents()


def get_task(index):
    major = index.split('.')[0]
    subkey = None
    key = None
    for line in toc.split('\n'):
        if line.startswith(f'{major}.'):
            key = line[len(major) + 2:]
        if line.strip().startswith(index):
            subkey = line.strip()[len(index) + 2:]
    if not (subkey and key):
        raise KeyError('Такой задачи нет')
    return tasks[key][subkey]


def get_task_name(index):
    for line in toc.split('\n'):
        if line.strip().startswith(index.strip()):
            return line.strip()
    return index


def get_format_message(task):
    return '\n'.join(map(str, task['input_format']))


if __name__ == "__main__":
    print(toc)
    mytask = get_task('1.3')
    print(get_format_message(mytask))
