import numpy as np
import sympy as sp

from accurate_interpolation import *

# TODO переделать структуру файла, чтобы был блок __name__ == "__main__",
# убрать использование глобальных переменных, поработать над неймингом 
# функций и переменных

x = sp.Symbol('x')
f = x**3 + 6 * x**2 + 9 * x + 1

a = -3
b = 0

# ищется минимум

def print_number(a, ROUNDING_COUNT = 5):
    out = ''
    if(type(a) == int or type(a) == float):
        out += f'{round(a, ROUNDING_COUNT)}'
    else:
        out += f'{a} = {round(a.evalf(), ROUNDING_COUNT)}'
    return out

def bisect(f, a, b, iteration = 1, COUNT_ITERATIONS = 3):
    if(iteration > COUNT_ITERATIONS):
        print(f'Ну здесь остановимся, минимум будет в отрезке {a.evalf()}, {b.evalf()}')
        return
    func = sp.lambdify(x, f)
    delta = sp.Rational(1, 10)

    u1 = sp.Rational( a+b - delta, 2)
    u2 = sp.Rational( a+b + delta, 2)
    
    func1 = func(u1)
    func2 = func(u2)

    print(f'В точке u1 = {print_number(u1)}: {print_number(func1)}') 
    print(f'В точке u2 = {print_number(u2)}: {print_number(func2)}') 

    if(iteration == COUNT_ITERATIONS):
        print(f'Последний шаг, надо вибирать минимум: ', end='')
        if(func1 < func2):
            print(f'{print_number(u1)}')
        else:
            print(f'{print_number(u2)}')
        return

    if(func1 < func2):
        print(f'Так как на этом подотрезке функция возрастает, выбираем отрезок [a = {print_number(a)}, {print_number(u2)}]')
        return bisect(f, a, u2, iteration+1, COUNT_ITERATIONS)
    else:
        print(f'Так как на этом подотрезке функция убывает, выбираем отрезок [u1 = {print_number(u1)}, b = {print_number(b)}]')
        return bisect(f, u1, b, iteration+1, COUNT_ITERATIONS)

def golden_cut(f, a, b, iteration = 1, COUNT_ITERATIONS = 3):
    if(iteration > COUNT_ITERATIONS):
        print(f'Ну здесь остановимся, минимум будет в отрезке {a.evalf()}, {b.evalf()}')
        return
    print(f'{iteration})', end = ' ')
    func = sp.lambdify(x, f)
    u1 = a + sp.Rational( 382, 1000 ) * (b-a)
    u2 = a + sp.Rational( 618, 1000 ) * (b-a)
    
    func1 = func(u1)
    func2 = func(u2)

    print(f'В точке u1 = {print_number(u1)}: {print_number(func1)}') 
    print(f'В точке u2 = {print_number(u2)}: {print_number(func2)}') 

    if(iteration == COUNT_ITERATIONS):
        print(f'Последний шаг, надо вибирать минимум: ', end='')
        if(func1 < func2):
            print(f'{print_number(u1)}')
        else:
            print(f'{print_number(u2)}')
        return

    if(func1 < func2):
        print(f'Так как на этом подотрезке функция возрастает, выбираем отрезок [a = {print_number(a)}, {print_number(u2)}]')
        return golden_cut(f, a, u2, iteration+1, COUNT_ITERATIONS)
    else:
        print(f'Так как на этом подотрезке функция убывает, выбираем отрезок [u1 = {print_number(u1)}, b = {print_number(b)}]')
        return golden_cut(f, u1, b, iteration+1, COUNT_ITERATIONS)

def is_vipuklaya_troika(a, fa, b, fb, c, fc):
    return fa >= fb and fc >= fb and fa + fc >= 2 * fb

def parabola(f, a, b):
    func = sp.lambdify(x, f)
    h = 0.2
    us = [ (a+b)/ 2. ]
    funcus = [ func(us[0]) ]

    print(f' us[0] = {print_number(us[0])}, f = {print_number(us[0])}. ')
    
    us.append(us[0] + h)
    funcus.append(func(us[-1]))
    print(f' us[1] = {print_number(us[1])}, f = {print_number(us[1])}. ')

    if(funcus[-1] > funcus[0]):
        print('Шагаем в другую сторону')
        us[1] = (us[0] - h)
        funcus[1] = func(us[-1])
        print(f' us[1] = {print_number(us[1])}, f = {print_number(us[1])}. ')

        i = 2
        while(True):
            us.append( us[0] - 2**(i-1) * h )
            funcus.append( func(us[-1]) )
            print(f'{i = }) u_{i} = {print_number(us[i])}')
            print(f'    f_{i} = {print_number(funcus[i])}')

            if(is_vipuklaya_troika(us[-1], funcus[-1]), us[-2], funcus[-2], us[-3], funcus[-3]):
                # make parabola
                coeff = naive_interpolation(us[-3:], funcus[-3:])
                print('Вершина параболки:',  - coeff[1] / (2 * coeff[-1]) )
                return 
            i += 1

    else:
        i = 2
        while(True):
            us.append( us[0] + 2**(i-1) * h )
            funcus.append( func(us[-1]) )
            print(f'{i = }) u_{i} = {print_number(us[i])}')
            print(f'    f_{i} = {print_number(funcus[i])}')

            if(is_vipuklaya_troika(us[-3], funcus[-3], us[-2], funcus[-2], us[-1], funcus[-1])):
                # make parabola
                coeff = inter_v_lob(us[-3:], funcus[-3:])
                print('Вершина параболки:',  - coeff[1] / (2 * coeff[-1]) )
                return 
            i += 1

def method_lomannih(f, a, b):
    pass
    # TODO

print('Метод деления отрезка пополам:')
bisect(f, a, b)

print('\n\nМетод золотого сечения:')
golden_cut(f, a, b)

print('\n\nМетод парабол:')
parabola(f, a, b)

print('\n\nМетод ломанных')
method_lomannih(f, a, b)



