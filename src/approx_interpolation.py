import numpy as np
import matplotlib.pyplot as plt

def mnk_interpolate(X, Y, power=1):
    F = np.matrix([[xi**pow for pow in range(power+1)] for xi in X])
    print(f'{F = }')
    FTF = F.T @ F
    print(f'{FTF = }')
    FTY = F.T @ Y
    print(f'{FTY = }')
    beta = FTF.I @ F.T @ Y
    beta = [i for i in np.array(beta[0])][0][::-1]
    print(f'{beta = }')
    
    p = np.poly1d(beta)
    print(p,'\n')
    return p

if __name__ == "__main__":
    X = np.array([
        -1,0,1,2
    ])
    Y = np.array([
        1,-1,2,-1
    ])

    p = mnk_interpolate(X, Y, 2)

    plt.scatter(X,Y,color='red')

    x = np.linspace(-3,3,1000)
    y = p(x)
    plt.plot(x,y)
    plt.show()

