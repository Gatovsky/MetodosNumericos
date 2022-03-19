import numpy as np


# fórmula:  x^(k+1) = (L + D)⁻¹(b - Ux^k)
def gausssiedel(A, b, x0, eps=1e-12, n=500):
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
        [17., -2., -3.],
        [-5., 21., -2.],
        [-5., -5., 22.]
    ])

    b = np.array([500, 200, 30])
    x0 = np.random.rand(3)
    x = gausssiedel(matriz, b, x0, 1e-12, 100)

    print("b calculado: ", np.dot(matriz, x))
    print("b verdadero: ", b)
    print("x1= {}  x2= {}  x3= {}".format(x[0], x[1], x[2]))


if __name__ == '__main__':
    main()
