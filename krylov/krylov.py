import numpy as np


def sistema(M, b, eps=1e-12, n=500):
    x = M
    for i in range(n):
        x_anterior = x
        x = np.linalg.inv(M).dot(b)

        if np.linalg.norm(x - x_anterior) < eps:
            return x

    return x


# fórmula: [A^(n-1)y, A^(n-2)y, ..., y]b = -A^(n)y
def krylov(A, y):
    Ay = np.dot(A, y)
    A2y = np.dot(A, Ay)
    A3y = np.dot(A, A2y)
    A4y = np.dot(A, A3y)
    #A5y = np.dot(A, A4y)

    # -A^(n)y
    b = np.dot(A4y, -1)
    # La nueva matriz está dada como una transpuesta
    M = np.array([A3y, A2y, Ay, y]).transpose()

    x = sistema(M, b)

    print("Ay = \n", Ay)
    print("A²y = \n", A2y)
    print("A³y = \n", A3y)
    #print("A⁴y = \n", A4y)
    #print("A⁴y = \n", A5y)

    print("b = \n", b)
    print("M = \n", M)

    print("λ⁴ {:+.6f}λ³ {:+.6f}λ² {:+.6f}λ {:+.6f}".format(x[0], x[1], x[2], x[3]))


def main():
    matriz = np.array([
                      [5, 2, 1, 0],
                      [-4, 0, 7, -1],
                      [6, -8, 2, 1],
                      [5, -3, -1, 6]
                       ])

    y = np.array([1, 0, 0, 0])

    B = np.array([
        [-1, 2, 2, 1, -2],
        [3, -6, -1, 5, -4],
        [2, -4, -1.5, 2, -1],
        [1, -2, 1, 1, 1],
        [5, 3, -1, -2, -2]
    ], dtype='float64')

    b = np.array([2, 1, -0.5, 1, 0])

    krylov(matriz, y)

    # krylov(B, b)


if __name__ == '__main__':
    main()
