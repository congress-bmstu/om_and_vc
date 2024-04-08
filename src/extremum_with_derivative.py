import numpy as np
import sympy as sp

try:
    from .utils import *
except:
    from utils import *

x = sp.Symbol('x')

def method_srednei_tochki(f, a, b, diff_f = None,
                          COUNT_ITERATIONS = 3, x = sp.Symbol('x')):
    if(diff_f is None):
        diff_f = sp.diff(f, x)
    for iteration in range(COUNT_ITERATIONS):
        diff_a = diff_f.subs(x, a)
        diff_b = diff_f.subs(x, b)

        c = sp.Rational(a+b, 2)
        diff_c = diff_f.subs(x, c)

        print(f"a_{iteration} = {print_number(a)}; diff_f(a_{iteration}) = {print_number(diff_a)}")
        print(f"b_{iteration} = {print_number(b)}; diff_f(b_{iteration}) = {print_number(diff_b)}")
        if(diff_a < 0 and diff_b < 0) or (diff_a > 0 and diff_b > 0):
            print("diff_a and diff_b must be same signs")
            return None

        print(f"c_{iteration} = {print_number(c)}; diff_f(c_{iteration}) = {print_number(diff_c)}")
        if(diff_c == 0):
            return c
        elif( (diff_c < 0 and diff_a > 0) or (diff_c > 0 and diff_a < 0) ):
            a = a
            b = c
        else:
            a = c
            b = b
    return c
        
def chordal_method(f, a, b, diff_f = None,
                   COUNT_ITERATIONS = 3, x = sp.Symbol('x')):
    if(diff_f is None):
        diff_f = sp.diff(f, x)
    for iteration in range(COUNT_ITERATIONS):
        diff_a = diff_f.subs(x, a)
        diff_b = diff_f.subs(x, b)

        print(f"a_{iteration} = {print_number(a)}; diff_f(a_{iteration}) = {print_number(diff_a)}")
        print(f"b_{iteration} = {print_number(b)}; diff_f(b_{iteration}) = {print_number(diff_b)}")
        if(diff_a < 0 and diff_b < 0) or (diff_a > 0 and diff_b > 0):
            print("diff_a and diff_b must be same signs")
            return None

        c = - diff_a * (b - a) / (diff_b - diff_a) + a
        diff_c = diff_f.subs(x, c)

        print(f"c_{iteration} = {print_number(c)}; diff_f(c_{iteration}) = {print_number(diff_c)}")
        if(diff_c == 0):
            return c
        elif( (diff_c < 0 and diff_a > 0) or (diff_c > 0 and diff_a < 0) ):
            a = a
            b = c
        else:
            a = c
            b = b
    return c

if __name__ == "__main__":
    f = x**3 + 6 * x**2 + 9 * x + 1
    a = -sp.Rational(5, 2)
    b = 0

    diff_f = sp.diff(f, x)
    print(f'{f = }')
    print(f'{diff_f = }')

    print('\n\nМетод средней точки')
    method_srednei_tochki(f, a, b, diff_f = diff_f)

    print('\n\nМетод секущих')
    chordal_method(f, a, b, diff_f)

