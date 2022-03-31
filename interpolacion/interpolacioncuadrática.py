import numpy as np
from grafica import graficaCuadratica


def interpolacionCuadratica(xi, yi, x):
    b0 = yi[0]
    b1 = (yi[1] - yi[0]) / (xi[1] - xi[0])
    b2 = (((yi[2] - yi[1]) / (xi[2] - xi[1])) - ((yi[1] - yi[0]) / (xi[1] - xi[0]))) / (xi[2] - xi[0])
    y = b0 + b1 * (x - xi[0]) + b2 * (x - xi[0]) * (x - xi[1])

    return y


def main():
    # conjuntos
    array_xi = [0.1, 0.4, 1.0, 1.3]
    array_yi = [0.99750, 0.96040, 0.76520, 0.62009]
    #np.array([0.1, 0.4, 1.0, 1.3]), np.array([0.99750, 0.96040, 0.76520, 0.62009])

    # tomar 3 valores donde x sea intermedio: a <= b <= x <= c
    # y los correspondientes a y: a <= b <= y? <= c
    x0 = array_xi[1]
    x1 = array_xi[2]
    x2 = array_xi[3]
    y0 = array_yi[1]
    y1 = array_yi[2]
    y2 = array_yi[3]
    x = 1.2

    tmp_xi = np.array([x0, x1, x2])
    tmp_yi = np.array([y0, y1, y2])

    y = interpolacionCuadratica(tmp_xi, tmp_yi, x)

    # nuevos conjuntos con los valores x, y
    # coloque x,y ordenadamente para evitar dibujar mal la línea de la gráfica
    array_x = np.array([0.1, 0.4, 1.0, x, 1.3])
    array_y = np.array([0.99750, 0.96040, 0.76520, y, 0.62009])

    graficaCuadratica(array_x, array_y, x, y)
    print("y=", y)


if __name__ == '__main__':
    main()
