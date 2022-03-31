import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def sistema(M, b, eps=1e-21, n=1000):
    x = M
    for i in range(n):
        x_anterior = x
        x = np.linalg.inv(M).dot(b)

        if np.linalg.norm(x - x_anterior) < eps:
            return x

    return x


def graph3d(vector):
    figura = plt.figure()
    ax = Axes3D(figura)

    x = np.linspace(-10, 10, 50)
    y = np.linspace(-10, 10, 50)

    X, Y = np.meshgrid(x, y)
    # Despeje de las z del sistema de ecuaciones
    Z1 = (1 - X - 2*Y) / 2
    Z2 = (5 - 3*X - Y) / 2
    Z3 = (8 - 4*X - 3*Y) / 3

    figura = plt.figure()
    ax = figura.add_subplot(111,projection='3d')
    ax.plot_surface(X, Y, Z1, alpha=0.5, cmap=cm.Accent, rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z2, alpha=0.5, cmap=cm.Paired, rstride=100, cstride=100)
    ax.plot_surface(X, Y, Z3, alpha=0.5, cmap=cm.Pastel1, rstride=100, cstride=100)
    ax.plot((vector[0],), (vector[1],), (vector[2],), lw= 2, c='k', marker='o',
            markersize=9, markeredgecolor='black')
    ax.plot((3,), (1,), (2,), lw=4, c='k', marker='*',
            markersize=9, markeredgecolor='white')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def main():
    # a, b, c = sp.symbols('a, b, c')

    # sistema = sp.linsolve([2*a + 4*b + 6*c - 22, 3*a - 8*b + 5*c - 27, -a + b + 2*c - 2], [a, b, c])

    # Obtener los valores de la solución dentro del finiteSet de Sympy
    # y pasar de fracciones a decimales
    # vector = np.array([sp.N(sistema.args[0][0]), sp.N(sistema.args[0][1]), sp.N(sistema.args[0][2])])
    # print(vector)

    M = np.array([[1, 2, 2],
                  [3, 1, 2],
                  [4, 3, 3]])

    b = np.array([1, 5, 8])

    # vector = sistema(M, b)
    # print(vector)

    # graph3d(vector)

    B = np.array([
        [-1, 2, 2, 1, -2],
        [3, -6, -1, 5, -4],
        [2, -4, -1.5, 2, -1],
        [1, -2, 1, 1, 1],
        [5, 3, -1, -2, -2]
    ], dtype='float64')

    b2 = np.array([2, 1, -0.5, 1, 0])

    vector = sistema(B, b2)

    print(vector)


if __name__ == '__main__':
    main()