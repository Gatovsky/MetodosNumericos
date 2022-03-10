import math

import matplotlib as mpl
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
e = math.e
x2 = pow(-x, 2)
# e**(-x) - x
# -1 + 5.5 * x - 4 * x**2 + 0.5 * x**3

def grafica(x3):
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    ## mpl.rcParams['text.usetex'] = True  # permite usar Tex en nuestra grafica
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    x = np.linspace(-3, 3, 40)  # intervalo que será graficado

#   a considerar: para evitar 'ImmutableDenseNDimArray' object has no attribute '_eval_evalf'
#   el usuario deberá evitar mezclar funciones de la librería estándar de python, ejm. math.cos(x), math.exp(x), etc.
#   y usar las de Numpy np.cos(x), np.exp(x), o bien sympy.sympify(f)
    plt.plot(x, e**(-x**2) - x, color='orangered')
    plt.scatter(x3, 0, color='black')
    plt.axvline(x = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.axhline(y = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})

    plt.title('$f(x)= e^x² - x$',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["x"])

    plt.grid(True)
    plt.axis([-3, 3, -4, 4])  # intervalos de los ejes de la grafica
    plt.savefig("Examen2.png")
    plt.show()