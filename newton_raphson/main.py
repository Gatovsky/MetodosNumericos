import numpy as np
import pandas as pd
import sympy as sp
import grafica

x = sp.symbols('x')
#f = sp.exp(-x)-x
#f = -x**2 - 1.8 * x + 2.5
f = x**3 + 2 * x**2 + 10 * x - 20


def newtho_raphson(x0, es, imax, it, ea):
    xr = x0
    dx = sp.diff(f)
    fnr = x - (f / dx)
    mtrz_it = np.array([])
    mtrz_x0 = np.array([])
    mtrz_xr = np.array([])
    mtrz_es = np.array([])
    mtrz_ea = np.array([])

    while True:
        xr_anterior = xr
        xr = fnr.evalf(subs={x: xr_anterior})
        it += 1
        if xr != 0:
            ea = abs((xr - xr_anterior) / xr) * 100    # Error relativo porcentual aproximado

        test = f.evalf(subs={x: xr})
        mtrz_it = np.append(mtrz_it, it)
        mtrz_x0 = np.append(mtrz_x0, x0)
        mtrz_xr = np.append(mtrz_xr, xr)
        mtrz_es = np.append(mtrz_es, es)
        mtrz_ea = np.append(mtrz_ea, ea)

        if ea < es or it >= imax:
            break

    if test < 0.1:
        print(True, ": ", test)
    else:
        print(False, ": ", test)

    var_it = pd.Series(mtrz_it, name="it")
    var_x0 = pd.Series(mtrz_x0, name="x0")
    var_xr = pd.Series(mtrz_xr, name="xr")
    var_es = pd.Series(mtrz_es, name="es")
    var_ea = pd.Series(mtrz_ea, name="ea")

    tabla = pd.concat([var_it, var_x0, var_xr, var_es, var_ea], axis=1)
    print(tabla)

    return xr


def comprobacion(xr):
    return f.evalf(subs={x: xr})


def main():
    xr = newtho_raphson(24.6162, 1e-2, 5, 0, 100)
    grafica.grafica(xr)


if __name__ == '__main__':
    main()


