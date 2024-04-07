from src.accurate_interpolation import *
from src.approx_interpolation import *
from src.extremum_with_derivative import *
from src.extremum_with_two_derivatives import *
from src.extremum import *
# from src.multidim_optimization_with_grad import *
import sympy as sp

NUMBER_LIST = '1 2.2 3 -4 -5.1 //числа через пробел'
SINGLE_NUMBER = '2 //одно число'
FUNCTION = 'x**3 + 6 * x**2 + 9 * x + 1 // функция одной переменной x'

def parse_number(user_input):
    try:
        parsed_number = float(user_input)
        if parsed_number.is_integer():
            parsed_number = int(parsed_number)
        return parsed_number
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")

def parse_number_list(inp):
    return list(map(parse_number, inp.split()))

def process_by_template(inp, template, function):
    inputs = inp.split('\n')
    get_input = lambda: inputs.pop(0)
    args = []
    for token in template:
        if token == NUMBER_LIST:
            args.append(parse_number_list(get_input()))
        if token == SINGLE_NUMBER:
            args.append(parse_number(get_input()))
        if token == FUNCTION:
            parsed_function = sp.parse_expr(get_input(), evaluate=False)
            x = sp.symbols('x')
            parsed_function = sym_expr.subs('x', x)
            args.append(parsed_function)
    return function(*args)


tasks={
    'Точная интерполяция': {
        'Интерполяция в лоб':{
            'function': naive_interpolation,
            'input_format': [NUMBER_LIST, NUMBER_LIST]
        },
        'Интерполяция Лагранжа':{
            'function': lagrange_interpolation,
            'input_format': [NUMBER_LIST, NUMBER_LIST]
        },
        'Интерполяция Ньютона':{
            'function': newton_interpolation,
            'input_format': [NUMBER_LIST, NUMBER_LIST]
        }
    },
    'Приближенная интерполяция': {
        'Метод наименьших квадратов':{
            'function': mnk_interpolate,
            'input_format': [NUMBER_LIST, NUMBER_LIST, SINGLE_NUMBER],
        }
    },
    'Одномерная оптимизация без использования производной': {
        'Метод деления отрезка (почти) пополам': {
            'function': bisect,
            'input_format': [FUNCTION, SINGLE_NUMBER, SINGLE_NUMBER]
        },
        'Метод золотого сечения': {
            'function': golden_cut,
            'input_format': [FUNCTION, SINGLE_NUMBER, SINGLE_NUMBER]
        },
        'Метод парабол': {
            'function': parabola,
            'input_format': [FUNCTION, SINGLE_NUMBER, SINGLE_NUMBER]
        },
        'Метод ломанных': {
            'function': method_lomannih,
            'input_format': [FUNCTION, SINGLE_NUMBER, SINGLE_NUMBER, SINGLE_NUMBER]
        }
    }
}

def get_table_of_contents():
    i = 1
    toc = ''
    for key in tasks.keys():
        toc += f'{i}. {key}\n'
        j = 1
        for subkey in tasks[key].keys():
            toc += f'  {i}.{j}. {subkey}\n'
            j+=1
        i+=1
    return toc

toc = get_table_of_contents()

def get_task(index):
    major = index.split('.')[0]
    subkey = None
    key = None
    for line in toc.split('\n'):
        if line.startswith(f'{major}.'):
            key = line[len(major)+2:]
        if line.strip().startswith(index):
            subkey = line.strip()[len(index)+2:]
    if not (subkey and key):
        raise KeyError('Такой задачи нет')
    return tasks[key][subkey]

def get_format_message(task):
    return '\n'.join(task['input_format'])

if __name__ == "__main__":
    print(parse_number_list('1 2 3 1 2.2 3 -4 -5.1'))
    print(toc)
    mytask = get_task('1.6')
    print(get_format_message(mytask))