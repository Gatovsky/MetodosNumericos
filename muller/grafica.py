import matplotlib as mpl
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
# -1 + 5.5 * x - 4 * x**2 + 0.5 * x**3

def grafica(x2_1, x2_2, x2_3):
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    ## mpl.rcParams['text.usetex'] = True  # permite usar Tex en nuestra grafica
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    x = np.linspace(-2, 3, 40)  # intervalo que será graficado

#   a considerar: para evitar 'ImmutableDenseNDimArray' object has no attribute '_eval_evalf'
#   el usuario deberá evitar mezclar funciones de la librería estándar de python, ejm. math.cos(x), math.exp(x), etc.
#   y usar las de Numpy np.cos(x), np.exp(x), o bien sympy.sympify(f)
    plt.plot(x, x**5 -3.5 * x**4 + 2.75 * x**3 + 2.125* x**2 - 3.875 * x + 1.25, color='orangered')
    plt.scatter(x2_1, 0, color='black')
    plt.scatter(x2_2, 0, color='black')
    plt.scatter(x2_3, 0, color='black')
    plt.axvline(x = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.axhline(y = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})

    plt.title('$f(x)= x⁵ - 3.5x⁴ + 2.75x³ + 2.125x² - 3.875x + 1.25$',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["f(x)"])

    plt.grid(True)
    plt.axis([-2, 3, -5, 5])  # intervalos de los ejes de la grafica
    plt.savefig("Ejemplo4.png")
    plt.show()