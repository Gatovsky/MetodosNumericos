import numpy as np


# fórmula:  x^(k+1) = (L + D)⁻¹(b - Ux^k)
def gausssiedel(A, b, x0, eps=1e-12, n=100):
    D = np.diag(np.diag(A))

    L = np.tril(A, -1)
    U = np.triu(A, +1)
    x = x0
    for i in range(n):
        x_anterior = x
        x = np.dot(np.linalg.inv(L + D), (b - np.dot(U, x)))

        if np.linalg.norm(x - x_anterior) < eps:
            return x
    return x


def main():
    matriz = np.array([
        [70., 1, 0],
        [60, -1, 1],
        [40, 0, -1]
    ])

    # b = np.array([636, 518, 307])

    B = np.array([
        [-1, 2, 2, 1, -2],
        [3, -6, -1, 5, -4],
        [2, -4, -1.5, 2, -1],
        [1, -2, 1, 1, 1],
        [5, 3, -1, -2, -2]
    ], dtype='float64')

    b = np.array([2, 1, -0.5, 1, 0])

    #x0 = np.random.rand(3)
    #x = gausssiedel(matriz, b, x0, 1e-12, 100)

    x0 = np.random.rand(5)
    x = gausssiedel(B, b, x0)

    print("b calculado: ", np.dot(B, x))
    print("b verdadero: ", b)
    print("x1= {}  x2= {}  x3= {} x4= {} x5= {}".format(x[0], x[1], x[2], x[3], x[4]))


if __name__ == '__main__':
    main()
