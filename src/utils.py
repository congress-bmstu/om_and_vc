import sympy as sp

def print_number(a, ROUNDING_COUNT = 5, x = sp.Symbol('x')):
    out = ''
    if(type(a) == int or type(a) == float):
        out += f'{round(a, ROUNDING_COUNT)}'
    else:
        out += f'{a} = {round(a.evalf(), ROUNDING_COUNT)}'
    return out
