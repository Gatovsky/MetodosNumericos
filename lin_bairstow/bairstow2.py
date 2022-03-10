import sympy as sp
import numpy as np

import grafica


def raiz_cuadratica(r, s):
    disc = r ** 2 + 4 * s

    # mientras que disc no sea 0 se procede a sacar las raíces por
    # el método cuadrático
    if disc > 0:
        r1 = (r + sp.sqrt(disc)) / 2
        r2 = (r - sp.sqrt(disc)) / 2

        i1 = 0
        i2 = 0

    # si es 0 o menor para evitar indeterminanción
    else:
        r1 = r / 2
        r2 = r1
        i1 = sp.sqrt(abs(disc)) / 2
        i2 = -i1

    return r1, i1, r2, i2



def baisrtow(es, rr, ss, itmax):
    a = [1, -3.5, 2.75, 2.125, -3.875, 1.25]
    # a = [1, 2, 3, 4, 5, 1]
    nn = a.__len__()
    b = [0] * nn
    c = [0] * nn
    r = rr
    s = ss
    re = [0] * nn
    im = [0] * nn
    n = nn-1
    it = 0
    ea1 = 1
    ea2 = 1

    while n < 3 or it >= itmax:
        it = 0
        while ea1 <= es and ea2 <= es or it >= itmax:
            it += 1
            b[n] = a[n]
            b[n - 1] = a[n - 1] + r * b[n]
            c[n] = b[n]
            c[n - 1] = b[n - 1] + r * c[n]

            for i in range(n - 2, 0, -1):
                b[i] = a[i] + r * b[i + 1] + s * b[i + 2]
                c[i] = b[i] + r * c[i + 1] + s * c[i + 2]

            # determinante de c
            determinante = c[2] * (c[2] - c[3]) * c[1]

            # Cálculo de los incrementos de r y s
            if determinante != 0:
                deltaR = (-b[1] * c[2] + b[0] * c[3]) / determinante
                deltaS = (-b[0] * c[2] + b[1] * c[1]) / determinante
                r += deltaR
                s += deltaS

                # porcentaje de Error aproximado
                if r != 0:
                    ea1 = abs(deltaR / r) * 100
                    # print("ear: ", ea1)
                if s != 0:
                    ea2 = abs(deltaS / s) * 100
                    # print("eas: ", ea2)
            # reajuste de r y s si no es posible resolver las matrices
            # recordando que r y s tinen un valor inicial de -1
            # por tanto se reajustan a 0
            else:
                r += 1
                s += 1
                it = 0

            ###  cumplido que r y s tengan un error menor o igual al indicado (1%)
            ### se procede a buscar las raíces de la ecuación

            lst = raiz_cuadratica(r, s)
            re[n] = lst[0]      # r1
            im[n] = lst[1]      # i1
            re[n - 1] = lst[2]  # r2
            im[n - 1] = lst[3]  # i2

            n = n - 2

            for i in range(0, n):
                a[i] = b[i + 2]
                # print(a[i])

    if it < itmax:
        # [raiz1, i1, raiz2, i2]
        if n == 2:
            r = -a[1] / a[2]
            s = -a[0] / a[2]
            lst = raiz_cuadratica(r, s)
            re[n] = lst[0]      # r1
            im[n] = lst[1]      # i1
            re[n - 1] = lst[2]  # r2
            im[n - 1] = lst[3]  # i2

        else:
            re[n] = -a[0] / a[1]
            im[n] = 0
    else:
        it = 1

    print(it, itmax)

    return im, re

def main():
    lst_r = baisrtow(1e-7, -1, -1, 100)
    print(lst_r)
    grafica.grafica(lst_r)


if __name__ == '__main__':
    main()
