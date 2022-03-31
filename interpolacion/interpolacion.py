from grafica import graficaLineal
import numpy as np
import sympy as sp


def interpolacionLineal(x0, y0, x1, y1, x):
    y = ((y1 - y0) / (x1 - x0)) * (x - x0) + y0

    return y


def main():

    x0 = 1
    x1 = 25
    y0 = 3
    y1 = 35
    x = 17

    y = interpolacionLineal(x0, y0, x1, y1, x)

    lstx = np.array([x0, 5, 10, 15, x, 20, x1])
    lsty = np.array([y0, 9, 11, 20, y, 30, y1])

    graficaLineal(lstx, lsty)

    print("y = {} Btu/ft · h ·°F".format(y))

    print("\nPuntos coordenados\n")
    print("P({}, {}) R({}, {}) Q({}, {})".format(x0, y0, x, y, x1, y1))


if __name__ == '__main__':
    main()
