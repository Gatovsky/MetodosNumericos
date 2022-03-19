import numpy as np


def eliminacion(matriz, n):
    for i in range(0, n):
        if matriz[i][i] == 0:
            print("@Error")
            break
        for j in range(0, n):
            if i != j:
                ratio = matriz[j][i] / matriz[i][i]
                for k in range(0, n + 1):
                    matriz[j][k] = matriz[j][k] - (ratio * matriz[i][k])

    # calcular x, y, z
    for i in range(0, n):
        matriz[i][n] = matriz[i][n] / matriz[i][i]
        matriz[i][i] = 1

    print('\n'.join(['   '.join(['{:6}'.format(col) for col in fil]) for fil in matriz]))
    return matriz


def main():
    M = np.array([[2, -1, -2, -2],
                  [-1, 1, 1, 0],
                  [1, -2, 1, 8]], dtype='float64')

    m = eliminacion(M, 3)
    print("\nx: {}\ny: {}\nz: {}".format(m[0][3], m[1][3], m[2][3]))


if __name__ == '__main__':
    main()