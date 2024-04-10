from src.accurate_interpolation import *
from src.approx_interpolation import *
from src.extremum import *
from src.extremum_with_derivative import *
from src.extremum_with_two_derivatives import *

x = sp.Symbol('x')
f = x ** 3 - 3 * x + 1
a = 0
b = 3
x0 = 2

print("1.a)")
X = np.arange(a, b+1)
Y = [ f.subs(x, x_i) for x_i in X ]
print(f"{X = }; {Y = }")
print(f"{mnk_interpolate(X, Y, power=1) = }")
print("\n1.b)")
print(f"{mnk_interpolate(X, Y, power=2) = }")

print("\n\n")
print("Метод деления отрезка пополам")
print(f"{bisect(f, a, b, COUNT_ITERATIONS = 2) = }")

print("\nМетод золотого сечения")
print(f"{golden_cut(f, a, b, COUNT_ITERATIONS = 2) = }")

print("\nМетод парабол")
print(f"{parabola(f, a, b, h = sp.Rational(2, 10)) = }")

# три итерации это две итерации
print("\nМетод ломанных")
print(f"{method_lomannih(f, a, b, x0=x0, COUNT_ITERATIONS = 2) = }")

# две итерации это три итерации
print("\nМетод средней точки")
print(f"{method_srednei_tochki(f, a, b, diff_f=sp.diff(f, x), COUNT_ITERATIONS=3) = }")

print("\nМетод секущих")
print(f"{chordal_method(f, a, b, diff_f = sp.diff(f, x), COUNT_ITERATIONS=2) = }")

print("\nМетод Ньютона")
print(f"{newton_method(f, a, b, x0=x0, COUNT_ITERATIONS = 2) = }")
