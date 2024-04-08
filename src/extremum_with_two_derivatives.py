import sympy as sp
import numpy as np
import random

try:
    from .utils import *
except:
    from utils import *

def newton_method(f, a, b, diff_f = None, ddiff_f = None, x0 = None,
                  x = sp.Symbol('x'), COUNT_ITERATIONS = 8):
    if(diff_f is None):
        diff_f = sp.diff(f, x)
    if(ddiff_f is None):
        ddiff_f = sp.diff(diff_f, x)

    starting_point = -sp.Rational(5, 4) # random.random() * (b-a) + a
    if(x0 is None):
        x0 = sp.Rational(a+b, 2)
    x_k = x0
    for i in range(COUNT_ITERATIONS):
        diff_x_k = diff_f.subs(x, x_k)
        ddiff_x_k = ddiff_f.subs(x, x_k)
        print(f'x_{i} = {print_number(x_k)}')
        print(f"diff_f(x_{i}) = {print_number(diff_x_k)}")
        print(f"ddiff_f(x_{i}) = {print_number(ddiff_x_k)}")
        x_k = x_k - sp.Rational(diff_x_k, ddiff_x_k)
    if(len(str(x_k.denominator)) > 7):
        return x_k.evalf()
    else:
        return x_k

if __name__ == '__main__':
    x = sp.Symbol('x')
    f = x**3 + 6*x**2 + 9*x + 1
    newton_method(f, -1.9, 0, COUNT_ITERATIONS = 3)
