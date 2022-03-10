import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import sympy
import sympy as sp

x = sp.symbols('x')
f = x**10 - 1
g = x**10 - 1


def grafica():
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    ## mpl.rcParams['text.usetex'] = True  # permite usar Tex en nuestra grafica
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    x = np.linspace(-2, 2, 26)  # intervalo que será graficado

    plt.plot(x, x**10 - 1, color='tab:orange',
             marker='o')
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})

    plt.title('$f(x)= -25 + 82x -90x² + 44x³ - 8x⁴ + 0.7x⁵$',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["x1"])

    plt.grid(True)
    plt.axis([-2, 2, -2, 16])  # intervalos de los ejes de la grafica
    plt.savefig("Ejemplo1.png")
    plt.show()


def punto_medio(x0, es, imax, it, ea):
    xr = x0
    while True:
        xr_anterior = xr
        xr = g.evalf(subs={x: xr})
        it += 1
        if xr != 0:
            ea = abs((xr - xr_anterior) / xr) * 100
        if ea < es or it >= imax:
            break
    return xr


def main():
    print(punto_medio(0, 0.01, 5, 0, 100))
    grafica()


if __name__ == '__main__':
    main()
