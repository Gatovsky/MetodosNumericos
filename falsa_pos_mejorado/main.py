import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import sympy
import sympy as sp

x = sp.symbols('x')
#f = (9.8 * 68.1) / x * (1 - sp.exp(-x / 68.1 * 10)) - 40
#f = -25 + (82 * x) - (90 * x**2) + (44 * x**3) - (8 * x**4) + (0.7 * x**5)
f = -25 + (82 * x) - (90 * x**2) + (44 * x**3) - (8 * x**4) + (0.7 * x**5)
#f = x**10 - 1

def grafica():
    mpl.rcParams['figure.dpi'] = 150  # puntos por pulgada
    ## mpl.rcParams['text.usetex'] = True  # permite usar Tex en nuestra grafica
    mpl.rcParams['savefig.dpi'] = 200  # puntos por pulgada con lo que se guarda la grafica

    x = np.linspace(-6.125, 6, 60)  # en el intervalo 0,1 hasta 17 números arbitrarios

    plt.plot(x, -25 + (82 * x) - (90 * x**2) + (44 * x**3) - (8 * x**4) + (0.7 * x**5), color='tab:orange', marker='o')
    plt.xlabel('x', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.ylabel('y', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})

    plt.title('$f(x)= -25 + 82x -90x² + 44x³ - 8x⁴ + 0.7x⁵$', fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:green'})
    plt.legend(["x1"])

    plt.grid(True)
    plt.axis([-0.375, 2, -1, 16])  # intervalos de los ejes de la grafica
    plt.savefig("Ejemplo1.png")
    plt.show()


def falsa_pos_mejorada(xl, xu, es, imax, xr, it, ea):
    il = 0
    iu = 0
    it = 0
    mtrz_it = np.array([])
    mtrz_xl = np.array([])
    mtrz_xu = np.array([])
    mtrz_xr = np.array([])
    mtrz_ea = np.array([])

    fl = f.evalf(subs={x: xl})
    fu = f.evalf(subs={x: xu})
    while True:
        xr_anterior = xr
        xr = xu - fu * (xl - xu) / (fl - fu)
        fr = f.evalf(subs={x: xr})
        it += 1
        if xr < 0 or xr > 0:
            ea = abs((xr - xr_anterior) / xr) * 100
        aux = fl * fr

        mtrz_it = np.append(mtrz_it, it)
        mtrz_xl = np.append(mtrz_xl, xl)
        mtrz_xu = np.append(mtrz_xu, xu)
        mtrz_xr = np.append(mtrz_xr, xr)
        # global_mtrz_xr = np.append(mtrz_xr, xr)
        mtrz_ea = np.append(mtrz_ea, ea)

        if aux < 0:
            xu = xr
            fu = f.evalf(subs={x: xu})
            iu = 0
            il = il + 1
            if il >= 2:
                fl /= 2
        elif aux > 0:
            xl = xr
            fl = f.evalf(subs={x: xl})
            il = 0
            iu += 1
            if iu >= 2:
                fu /= 2
            else:
                ea = 0
        if ea < es or it > imax:
            break

    var_it = pd.Series(mtrz_it, name="it")
    var_xl = pd.Series(mtrz_xl, name="xl (a)")
    var_xu = pd.Series(mtrz_xu, name="xu (b)")
    var_xr = pd.Series(mtrz_xr, name="xr")
    var_ea = pd.Series(mtrz_ea, name="ea % (err relat. aprox)")

    tabla = pd.concat([var_it, var_xl, var_xu, var_xr, var_ea], axis=1)
    # return xr
    return tabla


def main():
    #                      xl, xu, es, imax, xr, it, ea
    a = falsa_pos_mejorada(0, 2, 0.02, 18, 0, 0, 100)
    grafica()
    print(a)


if __name__ == '__main__':
    main()

