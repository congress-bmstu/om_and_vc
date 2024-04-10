import pylab as p
import sympy as sp
import numpy as np
from sympy.matrices import Matrix, hessian

try:
    from .extremum_with_two_derivatives import newton_method 
    from .utils import *
except:
    from extremum_with_two_derivatives import newton_method 
    from utils import *

def grad_method_step_division(f, variables, alpha = sp.Rational(1, 2),
                              u0 = None, COUNT_ITERATIONS = 5):
    grad_f = [sp.diff(f, var1) for var1 in variables]
    
    if(u0 is None):
        u0 = [1 for var in variables]
    f_u = min_f = f.subs({var: u0[j] for (j,var) in enumerate(variables)})
    baru = u0

    u = u0
    f_k = f.subs({var: u[j] for (j,var) in enumerate(variables)})
    gradf_k = [ grad_comp.subs({var: u[j] for (j,var) in enumerate(variables)})
               for grad_comp in grad_f]
    print(f'u_{0} = {print_point(u)}')
    print(f'f(u_{0}) = {print_number(f_k)}')
    print(f'grad_f(u_{0}) = {print_point(gradf_k)}')

    for i in range(1, COUNT_ITERATIONS+1):
        u = [u[j] - alpha * gradf_k[j] for j in range(len(variables))]
        f_k = f.subs({var: u[j] for (j,var) in enumerate(variables)})
        gradf_k = [ grad_comp.subs({var: u[j] for (j,var) in enumerate(variables)})
                   for grad_comp in grad_f]
        print(f'u_{i} = {print_point(u)}')
        print(f'f(u_{i}) = {print_number(f_k)}')
        print(f'grad_f(u_{i}) = {print_point(gradf_k)}')

        if(f_k < min_f):
            min_f = f_k
            baru = u
        else:
            alpha = sp.Rational(alpha, 2)
    return (baru, min_f)

def grad_method_of_fastest_fall(f, variables, alpha = sp.Rational(1, 2),
                                u0 = None, COUNT_ITERATIONS = 5):
    grad_f = [sp.diff(f, var1) for var1 in variables]
    
    if(u0 is None):
        u0 = [1 for var in variables]
    f_u = min_f = f.subs({var: u0[i] for (i,var) in enumerate(variables)})
    baru = u0

    u = u0
    f_k = f.subs({var: u[j] for (j,var) in enumerate(variables)})
    gradf_k = [ grad_comp.subs({var: u[j] for (j,var) in enumerate(variables)})
               for grad_comp in grad_f]
    print(f'u_{0} = {print_point(u)}')
    print(f'f(u_{0}) = {print_number(f_k)}')
    print(f'grad_f(u_{0}) = {print_point(gradf_k)}')

    for i in range(1, COUNT_ITERATIONS+1):
        phi = f.subs({var: u[j] - sp.Symbol('alpha') * gradf_k[j]
                      for (j,var) in enumerate(variables)})
        print(f"phi_{i-1} = {phi}")
        print("Найдём минимум этой функции методом Ньютона:")
        alpha = newton_method(phi, -100, 100, x = sp.Symbol('alpha'), COUNT_ITERATIONS = 3)
        print("\n")
        print(f"alpha_{i-1} = {print_number(alpha)}", "\n")

        u = [u[j] - alpha * gradf_k[j] for j in range(len(variables))]
        f_k = f.subs({var: u[j] for (j,var) in enumerate(variables)})
        gradf_k = [ grad_comp.subs({var: u[j] for (j,var) in enumerate(variables)})
                   for grad_comp in grad_f]
        print(f'u_{i} = {print_point(u)}')
        print(f'f(u_{i}) = {print_number(f_k)}')
        print(f'grad_f(u_{i}) = {print_point(gradf_k)}')
    return (u, f_k)

def method_of_conjugate_directions(f, variables,
                                    u0 = None, COUNT_ITERATIONS = 5):
    grad_f = [sp.diff(f, var1) for var1 in variables]

    if (u0 is None):
        u0 = [1 for var in variables]
    f_u = min_f = f.subs({var: u0[i] for (i, var) in enumerate(variables)})
    baru = u0

    u = u0
    f_k = f.subs({var: u[j] for (j, var) in enumerate(variables)})
    Asp = hessian(f, variables)
    xy = (x, y)
    A = sp.lambdify(xy, Asp, modules='numpy')
    A = A(0, 0)
    grad_f = [sp.diff(f, var1) for var1 in [x, y]]
    print("A: ", A)
    b = [-grad_f[0].subs(y, 0).subs(x, 0), -grad_f[1].subs(x, 0).subs(y, 0)]
    print("b: ", b)
    p = []
    for i in range(1, COUNT_ITERATIONS + 1):
        Q = A @ u - b
        p.append(Q)
        if i == 1:
            alpha = (Q @ p[i - 1]) / ((A @ p[i - 1]) @ p[i - 1])
            u = u - alpha * p[i - 1]
            print(f"p_{i - 1} = {p}")
            print(f"alpha_{i - 1} = {alpha}")
            print(f"u_{i} = {u}")
        else:
            Q = A @ u - b
            beta = ((A @ p[i - 2]) @ Q) / ((A @ p[i - 2]) @ p[i - 2])
            alpha = (Q @ p[i - 1]) / ((A @ p[i - 1]) @ p[i - 1])
            u = u - alpha * p[i - 1]
            print(f"alpha_{i - 1} = {alpha}")
            print(f"beta_{i - 1} = {alpha}")
            print(f"p_{i - 1} = {p}")
            print(f"u_{i} = {u}")
        baru = u
        f_k = f.subs({var: u[j] for (j,var) in enumerate(variables)})
    return (baru, f_k)

if __name__ == '__main__': 
    x, y = sp.symbols('x, y')
    f = x**2 + 2 * y**2 + 2 * x * y - 2 * x - 4 * y
    # print('\nГрадиентный метод деления шага:')
    # print(f"{grad_method_step_division(f, [x, y], u0=[1, 2]) = }")
    #
    # print('\nГрадиентный метод наискорейшего спуска:')
    # grad_method_of_fastest_fall(f, [x, y])

    print('\nМетод сопряженных направлений:')
    print(f"{method_of_conjugate_directions(f, [x, y], u0=[1, 2], COUNT_ITERATIONS=2) = }")
