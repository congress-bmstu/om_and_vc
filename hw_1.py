from src.accurate_interpolation import *
from src.approx_interpolation import *
from src.extremum import *

x = sp.Symbol('x')
f = x**3 + 3*x**2 + 1
a = -1
b = 2

print("1.a)")
X = np.arange(a, b+1)
Y = [ f.subs(x, x_i) for x_i in X ]
print(f"{X = }; {Y = }")
print(f"{mnk_interpolate(X, Y, power=1) = }")
print("\n1.b)")
print(f"{mnk_interpolate(X, Y, power=2) = }")

print("\n\n")
print(f"{bisect(f, a, b, COUNT_ITERATIONS = 2) = }")


