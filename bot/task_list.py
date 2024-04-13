from src.accurate_interpolation import naive_interpolation, lagrange_interpolation, newton_interpolation
from src.approx_interpolation import mnk_interpolate
from src.extremum import bisect, golden_cut, parabola, method_lomannih
from src.extremum_with_derivative import method_srednei_tochki, chordal_method
from src.extremum_with_two_derivatives import newton_method
from src.multidim_optimization_with_grad import grad_method_step_division, grad_method_of_fastest_fall, \
    method_of_conjugate_directions

from bot.user_input import ArgumentInput
from bot.user_input import (NUMBER_LIST,
                            SINGLE_NUMBER,
                            FUNCTION,
                            VARIABLE,
                            VARIABLE_LIST,
                            POINT_2D)

tasks = {
    'Точная интерполяция': {
        'Интерполяция в лоб': {
            'function': naive_interpolation,
            'input_format': [
                ArgumentInput(NUMBER_LIST, 'X'),
                ArgumentInput(NUMBER_LIST, 'Y')
            ],
        },
        'Интерполяция Лагранжа': {
            'function': lagrange_interpolation,
            'input_format': [
                ArgumentInput(NUMBER_LIST, 'X'),
                ArgumentInput(NUMBER_LIST, 'Y')
            ]
        },
        'Интерполяция Ньютона': {
            'function': newton_interpolation,
            'input_format': [
                ArgumentInput(NUMBER_LIST, 'X'),
                ArgumentInput(NUMBER_LIST, 'Y')
            ]
        }
    },
    'Приближенная интерполяция': {
        'Метод наименьших квадратов': {
            'function': mnk_interpolate,
            'input_format': [
                ArgumentInput(NUMBER_LIST, 'X'),
                ArgumentInput(NUMBER_LIST, 'Y'),
                ArgumentInput(SINGLE_NUMBER, 'степень')
            ],
        }
    },
    'Одномерная оптимизация без использования производной': {
        'Метод деления отрезка (почти) пополам': {
            'function': bisect,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b')
            ]
        },
        'Метод золотого сечения': {
            'function': golden_cut,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b')
            ]
        },
        'Метод парабол': {
            'function': parabola,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b')
            ]
        },
        'Метод ломанных': {
            'function': method_lomannih,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b'),
                ArgumentInput(SINGLE_NUMBER, 'точка x0')
            ]
        }
    },
    'Одномерная оптимизация с использованием производных': {
        'Метод средней точки': {
            'function': method_srednei_tochki,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b')
            ]
        },
        'Метод хорд (метод секущих)': {
            'function': chordal_method,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b')
            ]
        },
        'Метод Ньютона (метод касательных)': {
            'function': newton_method,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(SINGLE_NUMBER, 'точка a'),
                ArgumentInput(SINGLE_NUMBER, 'точка b')
            ]
        },
    },
    'Многомерная оптимизация': {
        'Градиентный метод дробления шага': {
            'function': grad_method_step_division,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(VARIABLE_LIST, 'по которым производные'),
                ArgumentInput(POINT_2D, 'u0 исходная точка')
            ]
        },
        'Градиентный метод скорейшего спуска': {
            'function': grad_method_of_fastest_fall,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(VARIABLE_LIST, 'по которым производные'),
            ],
        },
        'Метод сопряженных направлений': {
            'function': method_of_conjugate_directions,
            'input_format': [
                ArgumentInput(FUNCTION, 'исходная функция'),
                ArgumentInput(VARIABLE_LIST, 'по которым производные'),
                ArgumentInput(POINT_2D, 'u0 исходная точка')
            ],
        }
    }
}
