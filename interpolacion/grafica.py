import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def graficaLineal(X, Y):
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    etiquetas = ["P", "R", "Q"]

    plt.plot(X,Y, ":", linewidth=2 ,color='firebrick')
    plt.plot(X, Y, "o", color="dodgerblue")

    for i, label in enumerate(etiquetas):
        plt.annotate(label, (X[i], Y[i]))

    plt.xlabel('x', fontdict={'fontsize': 13, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.ylabel('y', fontdict={'fontsize': 13, 'fontweight': 'bold', 'color': 'tab:green'})

    plt.title('conductividad térmica del agua a 95° F',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.legend(["f(x)"])


    plt.grid(True)
    #plt.axis([0, 25, 0, 45])  # intervalos de los ejes de la grafica
    plt.savefig("lineal1.png")
    plt.show()


def graficaCuadratica(X, Y, x, y):
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica


    plt.plot(X,Y, ":", linewidth=2 ,color='firebrick')
    plt.plot(X, Y, "o", color="dodgerblue")

    plt.plot(x,y, "o", color="orange")

    plt.xlabel('x', fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.ylabel('y', fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})

    plt.title('Interpolación Cuadrática',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})


    plt.grid(True)
    #plt.axis([0, 25, 0, 45])  # intervalos de los ejes de la grafica
    plt.savefig("cuadratica.png")
    plt.show()


def grafica(xi, fi, p_xi, p_fi, polinomioSimple):
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['savefig.dpi'] = 200

    plt.plot(xi, fi, "o", color="dodgerblue")
    plt.plot(p_xi, p_fi, ":", color="firebrick", linewidth=2)

    # valores x,y determinados por la interpolación cuadrática
    # se realiza la comparación del punto R(x,y) dado por el método cuadrático
    # y la función polinómica resuelta por Lagrange
    plt.plot(1.2, 0.6719792592592593, "o", color="orange")

    plt.title(polinomioSimple, fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.grid(True)
    plt.savefig("Lagrange_comparacion.png")
    plt.show()