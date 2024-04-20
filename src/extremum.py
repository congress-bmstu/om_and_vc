import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

try:
    from .utils import *
    from .accurate_interpolation import *
except:
    from accurate_interpolation import *
    from utils import *

# ищется минимум

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
            m = f_left
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

def golden_cut(f, a, b, COUNT_ITERATIONS = 3, x = sp.Symbol('x'),
               const_1 = sp.Rational( 381966011, 1000000000 )):
    const_2 = 1 - const_1
    # константа const_1 является приближением числа (3-sqrt(5))/2
    # = 0.381 966 011 - в зависимости от нужной в задаче точности (и возможности
    # использования обыкновенных дробей), в семинарах мы округляли до 381 / 1000

    tmpu = None # TODO доделать сохранение промежуточных точек, сместить за счёт этого 
    # нумерацию
    
    print(f"a_{0} = {print_number(a)}")
    print(f"b_{0} = {print_number(b)}")

    u_1 = a + const_1 * (b - a)
    u_2 = a + const_2 * (b - a)
    print(f"u_{1} = {print_number(u_1)}")
    print(f"u_{2} = {print_number(u_2)}")

    f_1 = f.subs(x, u_1)
    f_2 = f.subs(x, u_2)
    print(f"f(u_{1}) = {print_number(f_1)}")
    print(f"f(u_{2}) = {print_number(f_2)}")

    if(f_1 < f_2):
        a = a
        b = u_2
        tmpu = (True, u_1, f_1)
    else:
        a = u_1
        b = b
        tmpu = (False, u_2, f_2)
    print(f"a_{1} = {print_number(a)}")
    print(f"b_{1} = {print_number(b)}")
    print(f"baru_1 = u_{1 if tmpu[0] else 2} = {print_number(tmpu[1])}")

    for iteration in range(1, COUNT_ITERATIONS):
        u_n = a + b - tmpu[1]
        print(f"u_{iteration+2} = {print_number(u_n)}")
        f_n = f.subs(x, u_n)
        print(f"f(u_{iteration+2}) = {print_number(f_n)}")
        if( tmpu[1] < u_n ):
            if( tmpu[2] < f_n ):
                a = a
                b = u_n
                tmpu = ( True, tmpu[1], tmpu[2] )
            else:
                a = tmpu[1]
                b = b
                tmpu = (True, u_n, f_n)
        else:
            if( tmpu[2] < f_n ):
                a = u_n
                b = b
                tmpu = tmpu
            else:
                a = a
                b = tmpu[1]
                tmpu = (True, u_n, f_n)
        print(f"a_{iteration+1} = {print_number(a)}")
        print(f"b_{iteration+1} = {print_number(b)}")
        print(f"baru_{iteration+1} = {print_number(tmpu[1])}")
    print(f"m_* = {print_number(tmpu[2])}")
    return (tmpu[1], tmpu[2])

def is_vipuklaya_troika(u):
    u = sorted(u, key = lambda x: x[0])
    print(u)
    return u[0][1] >= u[1][1] and u[2][1] >= u[1][1] and u[0][1] + u[2][1] >= 2 * u[1][1]

def parabola(f, a, b, h = sp.Rational(1, 5), x0=None, x = sp.Symbol('x')):
    func = sp.lambdify(x, f)
    h = sp.Rational(2, 10)
    u = [ (x0 if x0 is not None else sp.Rational(a+b, 2), None) ]
    u[0] = (u[0][0], f.subs(x, u[0][0]))

    print(f'u_0 = {print_number(u[0][0])}, f_0 = {print_number(u[0][1])}. ')
    
    u.append( (u[0][0] + h, f.subs(x, u[0][0] + h)))
    print(f'u_1 = {print_number(u[1][0])}, f = {print_number(u[1][1])}. ')

    is_step_left = False
    if(u[1][1] > u[0][1]):
        is_step_left = True
        print("Будем двигаться влево")
        u[0], u[1] = u[1], u[0]
        print("Переобозначим точки:")
        print(f'u_0 = {print_number(u[0][0])}, f_0 = {print_number(u[0][1])}.')
        print(f'u_1 = {print_number(u[1][0])}, f_1 = {print_number(u[1][1])}.')

    while( (is_step_left and u[0][0] - h*2**(len(u) - 1) < b) or 
          (not is_step_left and u[0][0] + h*2**(len(u) - 1) > a) ):
        if(is_step_left):
            u.append( (u[0][0] - h*2**(len(u) - 1),
                       f.subs(x, (u[0][0] - h*2**(len(u) - 1))) ) )
        else:
            u.append( (u[0][0] + h*2**(len(u) - 1),
                       f.subs(x, (u[0][0] + h*2**(len(u) - 1))) ) )
        print(f'u_{len(u)-1} = {print_number(u[-1][0])}, f = {print_number(u[-1][1])}. ')
        if(is_vipuklaya_troika(u[-3:])):
            parabola = naive_interpolation([x[0] for x in u[-3:]], [x[1] for x in u[-3:]], x=x)
            print(f"{parabola}")
            omega = sp.solve(sp.Eq(sp.diff(parabola, x), 0), x)[0]
            print(f'Вершина параболки: {print_number(omega)}' )
            return (omega, f.subs(x, omega))
    return a if is_step_left else b
 

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
    expr_set = sorted(expr_set, key = lambda y : y[1].inf)
    expr_set_2 = sorted(expr_set_2, key = lambda y : y[1].inf)
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
                    COUNT_ITERATIONS = 3, plot_filename=None):
    if L is None:
        f_diff_lambda = sp.lambdify(x, sp.diff(f, x))
        L = max([ abs(f_diff_lambda(i)) for i in range(int(a), int(b)+1) ])
    print(f'{L = }')
    if x0 is None:
        x0 = sp.Rational(a+b, 2)
    u = sp.Symbol('u')
    g = sp.Piecewise((f.subs(x, u) + L * (x-u), (a <= x) & (x < u) ),
                     (f.subs(x, u) - L * (x-u), (x >= u) & (x <= b) ))
    xi = [x0]
    ps = [g.subs(u, x0)]
    print(f"x_{0} = {print_number(xi[-1])}")
    print("p_{0}")
    sp.pprint(ps[-1])

    styles = ['--',':','-']
    if plot_filename is not None:
        x_plot = np.linspace(a,b,100)
        y_plot = sp.lambdify(x,ps[-1], 'numpy')(x_plot)
        plt.plot(x_plot,y_plot, linestyle=styles[0], lw=2, label='$ p_0 $')
        
    for i in range(COUNT_ITERATIONS):
        xi.append( find_piecewise_min(ps[-1], a, b, x=x) )
        print(f"{i+1}) x_{i} = {print_number(xi[-1])}")

        ps.append( max_piecewise(ps[-1], g.subs(u, xi[-1]), xi[-1], x=x) )

        print(f"p_{i}")
        sp.pprint(ps[-1])
        
        if plot_filename is not None:
            y_plot = sp.lambdify(x,ps[-1], 'numpy')(x_plot)
            plt.plot(x_plot,y_plot, linestyle=styles[i+1], lw=(i+1)*5, alpha=1/(i+1),label=f'$ p_{i+1} $')
    xi.append( find_piecewise_min(ps[-1], a, b, x=x) )

    if plot_filename is not None:
        plt.xlabel('$ x $', loc='right')
        plt.ylabel('$ f $', loc='top', rotation=0)
        plt.plot(x_plot, sp.lambdify(x,f,'numpy')(x_plot), label=f'$ f(x)={sp.latex(f)} $')
        plt.scatter(xi[-1], f.subs(x, xi[-1]),c='r', label=f'$ min^*  $')
        plt.legend()
        plt.tight_layout()
        # plt.show()
        plt.savefig(plot_filename, dpi=300)
    return (xi[-1], f.subs(x, xi[-1]))

    

if __name__ == "__main__":
    x = sp.Symbol('x')
    f = x**3 + 6 * x**2 + 9 * x + 1
    a = -3
    b = 0

    print('Метод деления отрезка пополам:')
    bisect(f, a, b)

    print('\n\nМетод золотого сечения:')
    golden_cut(f, a, b, const_1 = sp.Rational(382, 1000))

    print('\n\nМетод парабол:')
    parabola(f, a, b)

    print('\n\nМетод ломанных')
    method_lomannih(f, a, b, x0=-2)



