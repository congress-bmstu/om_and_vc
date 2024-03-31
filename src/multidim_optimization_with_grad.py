import sympy as sp
import numpy as np

from extremum_with_two_derivatives import newton_method 

def grad_method_step_division(f, variables, alpha = sp.Rational(1, 2)):
    COUNT_ITERATIONS = 5
    f_lambda = sp.lambdify(variables, f)
    f_grad = [sp.diff(f, var1) for var1 in variables]
    f_grad_lambda = [sp.lambdify(variables, f_grad_1) for f_grad_1 in f_grad]

    x_k = 1
    y_k = 2
    min_f = 1e6

    for i in range(COUNT_ITERATIONS):
        print(f'(x_{i} = {x_k} = {round(x_k, 5)};  y_{i} = {y_k} = {round(y_k, 5)})')
        f_k = f_lambda(x_k, y_k)
        print(f'  f(x_{i}, y_{i}) = {f_k} = {round(f_k, 5)}')

        if(f_k < min_f):
            min_f = f_k
        else:
            alpha = sp.Rational(alpha, 2)

        x_k = x_k - alpha * f_grad_lambda[0](x_k, y_k)
        y_k = y_k - alpha * f_grad_lambda[1](x_k, y_k)

def grad_method_of_fastest_fall(f, variables):
    COUNT_ITERATIONS = 5
    f_lambda = sp.lambdify(variables, f)
    f_grad = [sp.diff(f, var1) for var1 in variables]
    f_grad_lambda = [sp.lambdify(variables, f_grad_1) for f_grad_1 in f_grad]

    x_k = 1
    y_k = 2

    for i in range(COUNT_ITERATIONS):
        print(f'{i}) (x_{i} = {x_k} = {round(x_k, 5)};  y_{i} = {y_k} = {round(y_k, 5)})')
        f_k = f_lambda(x_k, y_k)
        print(f'  f(x_{i}, y_{i}) = {f_k} = {round(f_k, 5)}')

        phi = f_lambda(x_k - sp.Symbol('alpha') * f_grad_lambda[0](x_k, y_k),
                       y_k - sp.Symbol('alpha') * f_grad_lambda[1](x_k, y_k))
        alpha = newton_method(phi, sp.Symbol('alpha'), -100, 100)
        print(f'Найденный минимум находится в точке alpha = {alpha}')

        x_k = x_k - alpha * f_grad_lambda[0](x_k, y_k)
        y_k = y_k - alpha * f_grad_lambda[1](x_k, y_k)

if __name__ == '__main__': 
    x, y = sp.symbols('x, y')
    f = x**2 + 2 * y**2
    print('\nГрадиентный метод деления шага:')
    grad_method_step_division(f, [x, y])

    print('\nГрадиентный метод наискорейшего спуска:')
    grad_method_of_fastest_fall(f, [x, y])
