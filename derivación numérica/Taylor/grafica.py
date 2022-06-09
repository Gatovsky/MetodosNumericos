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

    fig, ax = plt.subplots()

    ax.plot(xi, fi, "o", color="dodgerblue", label='xi, f(xi)')
    ax.plot(p_xi, p_fi, ":", color="firebrick", linewidth=2, label='función polinómica')

    # valores x,y determinados por la interpolación cuadrática
    # se realiza la comparación del punto R(x,y) dado por el método cuadrático
    # y la función polinómica resuelta por Lagrange
    ax.plot(0.55, 2.68, "o", color="orange", label='x = 0.55')

    plt.title("Función Polinómica", fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    ax.grid(True)
    legend = ax.legend(loc='best', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('C2')
    plt.savefig("Lagrange_2.png")
    plt.show()


def grafica2(x_list, y_list, punto_coordenado):
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['savefig.dpi'] = 200
    fig, ax = plt.subplots()

    plt.title("Interpolación de Newton", fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.xlabel("x")
    plt.ylabel("y")

    ax.scatter(x_list, y_list, color="purple", linewidths=2, label='xi , f(xi)')
    ax.scatter(punto_coordenado[0], punto_coordenado[1], color="orange", linewidth=2, label='x = 0.55')
    legend = ax.legend(loc='lower right', shadow=True, fontsize='x-large')
    legend.get_frame().set_facecolor('C2')
    ax.grid(True)
    plt.show()
