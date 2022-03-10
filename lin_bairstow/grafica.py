import matplotlib as mpl
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
# -1 + 5.5 * x - 4 * x**2 + 0.5 * x**3

def grafica(lst):
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    ## mpl.rcParams['text.usetex'] = True  # permite usar Tex en nuestra grafica
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    x = np.linspace(-2, 3, 60)  # intervalo que será graficado

#   a considerar: para evitar 'ImmutableDenseNDimArray' object has no attribute '_eval_evalf'
#   el usuario deberá evitar mezclar funciones de la librería estándar de python, ejm. math.cos(x), math.exp(x), etc.
#   y usar las de Numpy np.cos(x), np.exp(x), o bien sympy.sympify(f)
    # 1, -3.5, 2.75, 2.125, -3.875, 1.25
    plt.plot(x, 3 * x**5, color='orangered')
    plt.scatter(lst[0], 0, color='red')
    plt.scatter(lst[1], 0, color='red')
    plt.scatter(lst[2], 0, color='red')
    plt.scatter(lst[3], 0, color='red')
    #plt.scatter(lst[4], 0, color='red')
    #plt.scatter(lst[0][0], 0, color='black')
    #plt.scatter(lst[1][0], 0, color='red')
    #plt.scatter(lst[0][1], 0, color='black')
    #plt.scatter(lst[1][1], 0, color='red')
    #plt.scatter(lst[0][2], 0, color='black')
    #plt.scatter(lst[1][2], 0, color='red')
    #plt.scatter(lst[0][3], 0, color='black')
    #plt.scatter(lst[1][3], 0, color='red')
    #plt.scatter(lst[0][4], 0, color='black')
    #plt.scatter(lst[1][4], 0, color='red')
    #plt.scatter(lst[0][5], 0, color='black')
    #plt.scatter(lst[1][5], 0, color='red')
    plt.axvline(x = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.axhline(y = 0 , color='dodgerblue', linewidth=2.5, linestyle="--")
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})

    plt.title('$f(x)= 3x⁵$',
              fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["f(x)"])

    plt.grid(True)
    plt.axis([-2, 3, -4, 4])  # intervalos de los ejes de la grafica
    plt.savefig("Ejemplo10.png")
    plt.show()