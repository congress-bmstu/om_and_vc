import sympy as sp
import numpy as np
import random

def newton_method(f, x, a, b):
    print('Ищется минимум функции:')
    sp.pprint(f)
    COUNT_ITERATIONS = 8
    f_lambda = sp.lambdify(x, f)

    f_diff = sp.diff(f, x)
    print('Производная этой функции:')
    sp.pprint(f_diff)
    f_diff_lambda = sp.lambdify(x, f_diff)

    f_diff_2 = sp.diff(f_diff, x)
    print('Вторая производная этой функции')
    sp.pprint(f_diff_2)
    f_diff_2_lambda = sp.lambdify(x, f_diff_2)

    starting_point = -sp.Rational(5, 4) # random.random() * (b-a) + a
    x_k = starting_point
    for i in range(COUNT_ITERATIONS):
        print(f'x_{i} = {x_k} = {round(x_k, 5)}')
        x_k = x_k - sp.Rational(f_diff_lambda(x_k), f_diff_2_lambda(x_k))
    if(len(str(x_k.denominator)) > 7):
        return x_k.evalf()
    else:
        return x_k

if __name__ == '__main__':
    x = sp.Symbol('x')
    f = x**3 + 6*x**2 + 9*x + 1
    newton_method(f, x, -1.9, 0)
