import sympy as sp
import numpy as np
from src.multidim_optimization_with_grad import *

x, y = sp.symbols('x y')
g = x ** 2 + 2 * y ** 2 + 3 * y

print(f"{g = }")
print("\nГрадиентный метод дробления шага")
print(f"{grad_method_step_division(g, [x, y], alpha=sp.Rational(1, 10), u0=[1, 2], COUNT_ITERATIONS=2)}")

print("\nГрадиентный метод наискорейшего спуска")
print(f"{grad_method_of_fastest_fall(g, [x, y], alpha=sp.Rational(1, 10), u0=[1, 2], COUNT_ITERATIONS=2)}")

print("\nГрадиентный метод сопряженных направлений")
print(f"{method_of_conjugate_directions(g, [x, y], u0=[1, 2], COUNT_ITERATIONS=2)}")
