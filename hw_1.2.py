import sympy as sp
from src.multidim_optimization_with_grad import *

x, y = sp.symbols('x y')
g = x**2 + 2 * y**2 + 3*x

print(f"{g = }")
print("\nГрадиентный метод дробления шага")
print(f"{grad_method_step_division(g, [x, y], alpha = sp.Rational(1, 10), u0=[1, 2], COUNT_ITERATIONS = 2)}")
