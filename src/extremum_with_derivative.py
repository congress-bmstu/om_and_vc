import numpy as np
import sympy as sp

x = sp.Symbol('x')

def method_srednei_tochki(f, diff_f, a, b, iteration = 1, COUNT_ITERATIONS = 3):
    if(iteration > COUNT_ITERATIONS):
        print(f'Ну здесь остановимся, минимум будет в отрезке ({a}, {b})')
        return (a+b)/2.
    c0 = (a+b)/2.
    print(f'c{iteration-1} = {c0}')
    dfc = diff_f(c0)
    print(f"f'(c{iteration-1}) = {diff_f(c0)}")
    if(dfc == 0):
        return c0
    elif(dfc < 0):
        return method_srednei_tochki(f, diff_f, c0, b, iteration+1)
    else:
        return method_srednei_tochki(f, diff_f, a, c0, iteration+1)

def chordal_method(f, diff_f, a, b, iteration = 1, COUNT_ITERATIONS = 3):
    if(iteration > COUNT_ITERATIONS):
        print(f'Ну здесь остановимся, минимум будет в отрезке ({a}, {b})')
        return (a+b)/2.
    diff_fa = diff_f(a)
    diff_fb = diff_f(b)
    c0 = - diff_fa * (b - a) / (diff_fb - diff_fa) + a
    print(f'c{iteration-1} = {c0}')
    dfc = diff_f(c0)
    print(f"f'(c{iteration-1}) = {diff_f(c0)}")
    if(dfc == 0):
        return c0
    elif(dfc < 0):
        return chordal_method(f, diff_f, c0, b, iteration+1)
    else:
        return chordal_method(f, diff_f, a, c0, iteration+1)

if __name__ == "__main__":
    f = x**3 + 6 * x**2 + 9 * x + 1
    a = -2.5
    b = 0

    diff_f = sp.diff(f, x)
    print(f'{f = }')
    print(f'{diff_f = }')

    print('\n\nМетод средней точки')
    method_srednei_tochki(sp.lambdify(x, f), sp.lambdify(x, diff_f), a, b)

    print('\n\nМетод секущих')
    chordal_method(sp.lambdify(x, f), sp.lambdify(x, diff_f), a, b)

