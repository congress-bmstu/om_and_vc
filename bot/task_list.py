from bot.user_input import NUMBER_LIST, SINGLE_NUMBER, FUNCTION, ArgumentInput
from src.accurate_interpolation import naive_interpolation, lagrange_interpolation, newton_interpolation
from src.approx_interpolation import mnk_interpolate
from src.extremum import bisect, golden_cut, parabola, method_lomannih
from src.extremum_with_derivative import method_srednei_tochki, chordal_method
from src.extremum_with_two_derivatives import newton_method

tasks = {
    'Точная интерполяция': {
        'Интерполяция в лоб': {
            'function': naive_interpolation,
            'input_format': [
                ArgumentInput(NUMBER_LIST, ''),
                ArgumentInput(NUMBER_LIST, '')
            ],
        },
        'Интерполяция Лагранжа': {
            'function': lagrange_interpolation,
            'input_format': [
                ArgumentInput(NUMBER_LIST, ''),
                ArgumentInput(NUMBER_LIST, '')
            ]
        },
        'Интерполяция Ньютона': {
            'function': newton_interpolation,
            'input_format': [
                ArgumentInput(NUMBER_LIST, ''),
                ArgumentInput(NUMBER_LIST, '')
            ]
        }
    },
    'Приближенная интерполяция': {
        'Метод наименьших квадратов': {
            'function': mnk_interpolate,
            'input_format': [
                ArgumentInput(NUMBER_LIST, ''),
                ArgumentInput(NUMBER_LIST, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ],
        }
    },
    'Одномерная оптимизация без использования производной': {
        'Метод деления отрезка (почти) пополам': {
            'function': bisect,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        },
        'Метод золотого сечения': {
            'function': golden_cut,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        },
        'Метод парабол': {
            'function': parabola,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        },
        'Метод ломанных': {
            'function': method_lomannih,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        }
    },
    'Одномерная оптимизация с использованием производных': {
        'Метод средней точки': {
            'function': method_srednei_tochki,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        },
        'Метод хорд (метод секущих)': {
            'function': chordal_method,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        },
        'Метод Ньютона (метод касательных)': {
            'function': newton_method,
            'input_format': [
                ArgumentInput(FUNCTION, ''),
                ArgumentInput(SINGLE_NUMBER, ''),
                ArgumentInput(SINGLE_NUMBER, '')
            ]
        },
    },
    # 'Многомерная оптимизация': {
    #     'Градиентный метод дробления шага': {
    #         'function': grad_method_step_division,
    #         'input_format': [
    #             UserInput(FUNCTION, '')
    #         ]
    #     },
    #     'Градиентный метод скорейшего спуска': {
    #         'function': grad_method_of_fastest_fall,
    #         'input_format': [
    #             UserInput(FUNCTION, '')
    #         ],
    #     },
    #     'Метод сопряженных направлений': {
    #         'function': lambda: 'Пока еще не реализовали',
    #         'input_format': [],
    #     }
    # }
}
