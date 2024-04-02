import numpy as np
import sympy as sp

def naive_interpolation(X, Y, x = sp.Symbol('x')):
    N = len(X)
    A = sp.Matrix([
        [ X[i]**j for j in range(N) ]
        for i in range(N)])
    print(f'{A = }')
    coeffs, = sp.linsolve( (A, sp.Matrix(Y)) )
    return sum([coeffs[i] * x**i for i in range(N)])

def lagrange_interpolation(X, Y, x = sp.Symbol('x')):
    N = len(X)
    y = 0
    for i in range(N):
        L = 1
        for j in range(N):
            if i==j:
                continue
            L *= (x - X[j])/ (X[i] - X[j])
        L = sp.simplify(L)
        sp.pprint(L)
        y += Y[i] * L
    y = sp.simplify(y)
    sp.pprint(y)
    return y

def newton_interpolation(X, Y, x = sp.Symbol('x')):
    N = len(X)
    A = [Y[0]]
    f = [A[0]]
    for i in range(1, N):
        L = 1
        for j in range(i):
            if i==j:
                continue
            L *= (x - X[j])

        if(isinstance(f[-1], int) or isinstance(f[-1], float) or isinstance(f[-1], np.int64)): 
            A.append( sp.Rational( (Y[i] - f[-1]), L.subs(x, X[i]) ) )
        else:
            A.append(
                    sp.Rational(
                        (Y[i] - f[-1].subs(x, (X[i])) ),
                        L.subs(x, X[i]) ) )

        f.append( f[-1] + A[-1] * L )
        sp.pprint(f[-1])
    print(A)
    return sp.simplify(f[-1])

if __name__ == '__main__':
    X = [-1, 0, 1, 2]
    Y = [1, -1, 2, -1]

    print(f'{naive_interpolation(X, Y) = }')
    print(f'{lagrange_interpolation(X, Y) = }')
    print(f'{newton_interpolation(X, Y) = }')
