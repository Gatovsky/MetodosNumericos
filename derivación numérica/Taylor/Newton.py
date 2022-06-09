'''
Nadie responde la pregunta? El editor en jefe creó un grupo QQ de aprendizaje y comunicación de Python: 579817333
 Buscando amigos con ideas afines para ayudarse entre sí, ¡también hay buenos tutoriales de aprendizaje en video y libros electrónicos en PDF en el grupo!
'''
import matplotlib.pyplot as plt
import numpy as np
import math
from grafica import grafica2


#  interpolación lagrange
def lagrange(x_, y, a):
    """
         Obtenga la interpolación de Lagrange
         : param x_: valor de lista de x
         : param y: valor de lista de y
         : param a: número a interpolar
         : return: devuelve el resultado de la interpolación
    """
    ans = 0.0
    for i in range(len(y)):
        t_ = y[i]
        for j in range(len(y)):
            if i != j:
                t_ *= (a - x_[j]) / (x_[i] - x_[j])
        ans += t_
    return ans


# Newton
def table(x_, y):
    """
         Obtener la tabla de interpolación de Newton
         : param x_: valor de la lista x
         : param y: valor de la lista y
         : return: vuelve a la tabla de interpolación
    """
    quotient = [[0] * len(x_) for _ in range(len(x_))]
    for n_ in range(len(x_)):
        quotient[n_][0] = y[n_]
    for i in range(1, len(x_)):
        for j in range(i, len(x_)):
            # j-i determina los elementos diagonales
            quotient[j][i] = (quotient[j][i - 1] - quotient[j - 1][i - 1]) / (x_[j] - x_[j - i])
    return quotient


def get_corner(result):
    """
         Obtenga elementos diagonales a través de la tabla de interpolación
         : resultado del parámetro: resultado de la tabla de interpolación
         : return: elemento diagonal
    """
    link = []
    for i in range(len(result)):
        link.append(result[i][i])
    return link


def newton(data_set, x_p, x_7):
    """
         Resultados de la interpolación de Newton
         : param data_set: diagonal del problema resuelto
         : param x_p: valor de entrada
         : param x_7: el valor de lista original de x
         : return: resultado de la interpolación de Newton
    """
    result = data_set[0]
    for i in range(1, len(data_set)):
        p = data_set[i]
        for j in range(i):
            p *= (x_p - x_7[j])
        result += p
    return result


def main():
    x = 0.55
    x_1 = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    y_1 = np.array([0, 2.12, 3.02, 3.25, 3.14, 2.85, 2.51, 2.16, 1.84])
    middle = table(x_1, y_1)
    n = get_corner(middle)

    new = newton(n, x, x_1)

    print("Interpolación de Newton: {}".format(new))

    grafica2(x_1, y_1, (x, new))


if __name__ == '__main__':
    main()
