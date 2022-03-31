from prettytable import PrettyTable
import numpy as np


def jacobi(A, b, x0, eps=1e-12, n=500):
    D = np.diag(np.diag(A))
    lu = A - D

    x = x0
    for i in range(n):
        d_inv = np.linalg.inv(D)
        x_anterior = x
        x = np.dot(d_inv, np.dot(-(lu), x) + b)

        if np.linalg.norm(x - x_anterior) < eps:
            return x
    return x


def jacobiMio(n, matriz):
    tabla = PrettyTable()

    x1 = 0.
    x2 = 0.
    x3 = 0.
    contador = 0
    ea = 1e-9
    while True:
        x1_anterior = x1
        x2_anterior = x2
        x3_anterior = x3

        x1 = (matriz[0][3] - matriz[0][1] * x2 - matriz[0][2] * x3) / matriz[0][0]
        x2 = (matriz[1][3] - matriz[1][0] * x1 - matriz[1][2] * x3) / matriz[1][1]
        x3 = (matriz[2][3] - matriz[2][0] * x1 - matriz[2][1] * x2) / matriz[2][2]

        err_x1 = (x1 - x1_anterior) / x1
        err_x2 = (x2 - x2_anterior) / x2
        err_x3 = (x3 - x3_anterior) / x3

        contador += 1

        if err_x1 <= ea and err_x2 <= ea and err_x3 <= ea:
            break

    tabla.field_names = ["x1", "x2", "x3"]
    tabla.add_row([x1, x2, x3])
    print(tabla)
    print(contador)
    print(matriz)
    print("L = \n", np.tril(matriz, -1))
    print("U = \n", np.triu(matriz, +1))


def main():
    matriz = np.array([
        [4., 1., 1.],
        [1., 3., 1.],
        [1., 1., 5.]
    ])

    b = np.array([9, 10, 18])
    x0 = np.random.rand(3)
    x = jacobi(matriz, b, x0, 1e-4, 30)

    print("b calculado: ", np.dot(B, x))
    print("b verdadero: ", b)
    print("x1= {}  x2= {}  x3= {}".format(x[0], x[1], x[2]))


if __name__ == '__main__':
    main()
