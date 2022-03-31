import numpy as np


def gauss_jordan(matriz, n):
    # Elminación gauss jordan
    for i in range(0, n):
        if matriz[i][i] == 0:
            print("@Error")
            break
        for j in range(0, n):
            if i != j:
                ratio = matriz[j][i] / matriz[i][i]
                for k in range(0, n + 1):
                    matriz[j][k] = matriz[j][k] - (ratio * matriz[i][k])
    # print(matriz)

    # calcular x, y, z
    for i in range(0, n):
        with np.errstate(divide='raise'):
            try:
                matriz[i][n] = matriz[i][n] / matriz[i][i]
            except FloatingPointError:
                matriz[i][n] = 0

        matriz[i][i] = 1

    print('\n'.join(['   '.join(['{:6}'.format(col) for col in fil]) for fil in matriz ]))
    return matriz


def main():
    A = np.array([[70, 1, 0, 636],
                  [60, -1, 1, 518],
                  [40, 0, -1, 307]], dtype='float64')

    B = np.array([
        [0.1, -0.6, 1, -1, 1],
        [-2, 0.3, -4, 0.1, 0],
        [1, 0.5, 0.1, -0.3, 1],
        [0.5, -0.3, 0.6, 0.7, -1]
    ], dtype='float64')

    # m = gauss_jordan(A, 3)
    m2 = gauss_jordan(B, 4)

    print("\nx1: {}\nx2: {}\nx3: {}\nx4: {}".format(m2[0][4], m2[1][4], m2[2][4], m2[3][4]))


if __name__ == '__main__':
    main()
