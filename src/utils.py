import sympy as sp

def print_number(a, ROUNDING_COUNT = 5, x = sp.Symbol('x')):
    out = ''
    if(type(a) == int or type(a) == float):
        out += f'{round(a, ROUNDING_COUNT)}'
    else:
        out += f'{a} = {round(a.evalf(), ROUNDING_COUNT)}'
    return out

def print_point(u, ROUNDING_COUNT = 5):
    return '(' + ', '.join([print_number(x) for x in u]) + ')'
