import matplotlib as mpl
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
# -1 + 5.5 * x - 4 * x**2 + 0.5 * x**3

def grafica(xr):
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    ## mpl.rcParams['text.usetex'] = True  # permite usar Tex en nuestra grafica
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    x = np.linspace(-2, 4, 40)  # intervalo que será graficado

    plt.plot(x, x**3 + 2 * x**2 + 10 * x - 20, color='orangered', marker='o')
    plt.scatter(xr, 0, color='black')
    plt.axvline(x = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.axhline(y = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})

    plt.title('$f(x)= x³ + 2x² + 10 x - 20$',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["x"])

    plt.grid(True)
    plt.axis([-1.25, 2.25, -5, 2])  # intervalos de los ejes de la grafica
    plt.savefig("Examen1.png")
    plt.show()