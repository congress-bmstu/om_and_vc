import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def mnk_interpolate(X, Y, power=1, x = sp.Symbol('x')):
    F = sp.Matrix([[xi**pow for pow in range(power+1)] for xi in X])
    print(f'{F = }')
    FTF = F.transpose() @ F
    print(f'FT * F = {FTF}')
    FTY = F.transpose() @ sp.Matrix(Y)
    print(f'FT * Y = {FTY}')
    beta = FTF.inv() @ FTY
    # beta = [i for i in np.array(beta[0])][0][::-1]
    print(f'{beta = }')
    
    # p = np.poly1d(beta)
    p = sum([ x**p * beta[p] for p in range(power+1) ])
    print(p,'\n')
    return p

if __name__ == "__main__":
    X = [
        -1,0,1,2
    ]
    Y = [
        1,-1,2,-1
    ]

    p = sp.lambdify(sp.Symbol('x'), mnk_interpolate(X, Y, 2))

    plt.scatter(X,Y,color='red')

    x = np.linspace(-3,3,1000)
    y = p(x)
    plt.plot(x,y)
    plt.show()

