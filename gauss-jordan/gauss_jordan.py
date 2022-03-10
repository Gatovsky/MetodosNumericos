import numpy as np


def gauss_jordan(n):
    matriz = np.zeros((n, n+1), dtype=float)

    # llenar matriz
    for i in range(0, n):
        for j in range(0, n+1):
            num = int(input("valor: "))
            matriz[i][j] = num

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
        matriz[i][n] = matriz[i][n] / matriz[i][i]
        matriz[i][i] = 1

    print('\n'.join(['   '.join(['{:6}'.format(col) for col in fil]) for fil in matriz ]))
    return matriz


def main():

    """lst = input("ns: ").split(" ")
    int_lst = list(map(int, lst))
    print(int_lst)"""

    m = gauss_jordan(3)

    print("x: {}\ny: {}\nz: {}".format(m[0][3], m[1][3], m[2][3]))


if __name__ == '__main__':
    main()
