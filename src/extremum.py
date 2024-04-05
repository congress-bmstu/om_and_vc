import numpy as np
import sympy as sp

try:
    from .accurate_interpolation import *
except:
    from accurate_interpolation import *

# ищется минимум

def print_number(a, ROUNDING_COUNT = 5, x = sp.Symbol('x')):
    out = ''
    if(type(a) == int or type(a) == float):
        out += f'{round(a, ROUNDING_COUNT)}'
    else:
        out += f'{a} = {round(a.evalf(), ROUNDING_COUNT)}'
    return out

def bisect(f, a, b, COUNT_ITERATIONS = 3,
           x = sp.Symbol('x'),
           delta = sp.Rational(1, 10)):
    print(f"a_{0} = {print_number(a)}")
    print(f"b_{0} = {print_number(b)}")
    for iteration in range(COUNT_ITERATIONS):
        u_left = sp.Rational( a+b - delta, 2)
        u_right = sp.Rational( a+b + delta, 2)
        print(f"u_{2*iteration+1} = {print_number(u_left)}")
        print(f"u_{2*iteration+2} = {print_number(u_right)}")
        f_left = f.subs(x, u_left)
        f_right = f.subs(x, u_right)
        print(f"f(u_{2*iteration+1}) = {print_number(f_left)}")
        print(f"f(u_{2*iteration+2}) = {print_number(f_right)}")
        if(f_left <= f_right):
            a = a
            b = u_right
            baru = u_left
            m = u_left
        else:
            a = u_left
            b = b
            baru = u_right
            m = f_right
        print(f"a_{iteration+1} = {print_number(a)}")
        print(f"b_{iteration+1} = {print_number(b)}")
    print(f"baru = {print_number(baru)}")
    print(f"m_* = {print_number(m)}")
    return (baru, m)

def golden_cut(f, a, b, COUNT_ITERATIONS = 3, x = sp.Symbol('x')):
    # if(iteration > COUNT_ITERATIONS):
    #     print(f'Ну здесь остановимся, минимум будет в отрезке {a.evalf()}, {b.evalf()}')
    #     return
    # print(f'{iteration})', end = ' ')
    # func = sp.lambdify(x, f)
    # u1 = a + sp.Rational( 382, 1000 ) * (b-a)
    # u2 = a + sp.Rational( 618, 1000 ) * (b-a)
    
    # func1 = func(u1)
    # func2 = func(u2)

    # print(f'В точке u1 = {print_number(u1)}: {print_number(func1)}') 
    # print(f'В точке u2 = {print_number(u2)}: {print_number(func2)}') 

    # if(iteration == COUNT_ITERATIONS):
    #     print(f'Последний шаг, надо вибирать минимум: ', end='')
    #     if(func1 < func2):
    #         print(f'{print_number(u1)}')
    #     else:
    #         print(f'{print_number(u2)}')
    #     return

    # if(func1 < func2):
    #     print(f'Так как на этом подотрезке функция возрастает, выбираем отрезок [a = {print_number(a)}, {print_number(u2)}]')
    #     return golden_cut(f, a, u2, iteration+1, COUNT_ITERATIONS)
    # else:
    #     print(f'Так как на этом подотрезке функция убывает, выбираем отрезок [u1 = {print_number(u1)}, b = {print_number(b)}]')
    #     return golden_cut(f, u1, b, iteration+1, COUNT_ITERATIONS)

    const_1 = sp.Rational( 381966011, 1000000000 )
    # константа const_1 является приближением числа (3-sqrt(5))/2
    # = 0.381 966 011
    const_2 = 1 - const_1

    tmpu = None # TODO доделать сохранение промежуточных точек, сместить за счёт этого 
    # нумерацию
    
    print(f"a_{0} = {print_number(a)}")
    print(f"b_{0} = {print_number(b)}")
    for iteration in range(COUNT_ITERATIONS):
        u_left = a + const_1 * (b - a)
        u_right = a + const_2 * (b - a)
        print(f"u_{2*iteration+1} = {print_number(u_left)}")
        print(f"u_{2*iteration+2} = {print_number(u_right)}")

        f_left = f.subs(x, u_left)
        f_right = f.subs(x, u_right)
        print(f"f(u_{2*iteration+1}) = {print_number(f_left)}")
        print(f"f(u_{2*iteration+2}) = {print_number(f_right)}")
        if(f_left < f_right):
            a = a
            b = u_right
            baru = u_left
            m = u_left
        else:
            a = u_left
            b = b
            baru = u_right
            m = f_right
        print(f"a_{iteration+1} = {print_number(a)}")
        print(f"b_{iteration+1} = {print_number(b)}")
    print(f"baru = {print_number(baru)}")
    print(f"m_* = {print_number(m)}")
    return (baru, m)

def is_vipuklaya_troika(a, fa, b, fb, c, fc):
    return fa >= fb and fc >= fb and fa + fc >= 2 * fb

def parabola(f, a, b, h = 0.2, x = sp.Symbol('x')):
    func = sp.lambdify(x, f)
    h = sp.Rational(2, 10)
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
                coeff = naive_interpolation(us[-3:], funcus[-3:])
                print('Вершина параболки:',  - coeff[1] / (2 * coeff[-1]) )
                return 
            i += 1


def find_piecewise_min(piecewise, a, b, x = sp.Symbol('x')):
    min_x = None
    min_piecewise = None
    for (piece, interval) in piecewise.as_expr_set_pairs():
        bounds = [interval.inf, interval.sup]
        for b in bounds:
            func_1 = piece.subs(x, b) 
            if(min_piecewise is None or func_1 < min_piecewise):
                min_x = b
                min_piecewise = func_1
    return min_x

def max_piecewise(piecewise_1, piecewise_2, point, x = sp.Symbol('x')):
    expr_set = list(piecewise_1.as_expr_set_pairs())
    expr_set_2 = list(piecewise_2.as_expr_set_pairs())
    # предполагается, что piecewise_2 состоит из двух интервалов с границей point
    interval_index = None
    is_going_down = None
    for (index, (piece, interval)) in enumerate(expr_set):
        if interval.contains(point):
            interval_index = index
            is_going_down = (sp.diff(piece, x) < 0)
            break
    if(interval_index is None):
        raise ValueError("Что-то пошло не так, не могу найти максимум ломанных")
    # print(f"{interval_index = }, {is_going_down = }")
    if(interval_index == 0 and not is_going_down):
        deleted = expr_set.pop(0)
        if(len(expr_set_2) == 1): # случай, когда sympy удалил левый подотрезок, потому
            # что точка point = a.
            x_1 = sp.solve(sp.Eq(deleted[0], expr_set_2[0][0]), x)[0]
            expr_set += [
                (expr_set_2[0][0], (deleted[1].inf <= x) & (x < x_1) ),
                (deleted[0],       (x_1 <= x) & (x < deleted[1].sup) )]
        else:
            x_1 = sp.solve(sp.Eq(deleted[0], expr_set_2[1][0]), x)[0]
            expr_set += [
                (expr_set_2[0][0], (deleted[1].inf <= x) & (x < point) ),
                (expr_set_2[1][0], (point <= x) & (x < x_1) ),
                (deleted[0],       (x_1 <= x) & (x < deleted[1].sup) )]
    elif(interval_index == len(expr_set)-1 and is_going_down):
        deleted = expr_set.pop(interval_index)
        x_1 = sp.solve(sp.Eq(deleted[0], expr_set_2[0][0]), x)[0]
        expr_set += [
            (deleted[0],       (deleted[1].inf <= x) & (x < x_1) ),
            (expr_set_2[0][0], (x_1 <= x) & (x < point) ),
            (expr_set_2[1][0], (point <= x) & (x < deleted[1].sup)) ]
    else:
        if(is_going_down):
            deleted_2 = expr_set.pop(interval_index+1)
            deleted_1 = expr_set.pop(interval_index)
        else:
            deleted_2 = expr_set.pop(interval_index)
            deleted_1 = expr_set.pop(interval_index-1)
        x_1 = sp.solve(sp.Eq(deleted_1[0], expr_set_2[0][0]), x)[0]
        x_2 = sp.solve(sp.Eq(deleted_2[0], expr_set_2[1][0]), x)[0]
        # print(expr_set)

        expr_set += [
                (deleted_1[0],    (deleted_1[1].inf <= x) & (x < x_1) ),
                (expr_set_2[0][0], (x_1 <= x) & (x < deleted_1[1].sup) ),
                (expr_set_2[1][0], (deleted_2[1].inf <= x) & (x < x_2) ),
                (deleted_2[0],     (x_2 <= x) & (x < deleted_2[1].sup) )]
    piecewise_args = [
        (piece, interval.contains(x) if isinstance(interval, sp.Interval) else interval)
        for (piece, interval) in expr_set]
    return sp.Piecewise(*piecewise_args)

def method_lomannih(f, a, b, x0=None, L = None,
                    x = sp.Symbol('x'),
                    COUNT_ITERATIONS = 5):
    if L is None:
        f_diff_lambda = sp.lambdify(x, sp.diff(f, x))
        L = max([ abs(f_diff_lambda(i)) for i in range(int(a), int(b)) ])
    print(f'{L = }')
    if x0 is None:
        x0 = sp.Rational(a+b, 2)
    u = sp.Symbol('u')
    g = sp.Piecewise((f.subs(x, u) + L * (x-u), (a <= x) & (x < u) ),
                     (f.subs(x, u) - L * (x-u), (x >= u) & (x <= b) ))
    xi = [x0]
    ps = [g.subs(u, x0)]
    for i in range(COUNT_ITERATIONS):
        print(f"{i+1}) x_{i} = {xi[i]}")
        print(f"p_{i}")
        sp.pprint(ps[-1])

        xi.append( find_piecewise_min(ps[-1], a, b, x=x) )
        ps.append( max_piecewise(ps[-1], g.subs(u, xi[-1]), xi[-1], x=x) )
    return xi[-1]

    

if __name__ == "__main__":
    x = sp.Symbol('x')
    f = x**3 + 6 * x**2 + 9 * x + 1
    a = -3
    b = 0

    print('Метод деления отрезка пополам:')
    bisect(f, a, b)

    print('\n\nМетод золотого сечения:')
    golden_cut(f, a, b)

    print('\n\nМетод парабол:')
    # parabola(f, a, b)

    print('\n\nМетод ломанных')
    method_lomannih(f, a, b, x0=-2)



