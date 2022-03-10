import numpy as np
import sympy as sp
import pandas as pd


def cambios_signo():
    x = sp.symbols('x')
    f = x**5 -3.5 * x**4 + 2.75 * x**3 + 2.125* x**2 - 3.875 * x + 1.2

    mtz_i = np.array([])
    mtz_fx = np.array([])
    lst = list()

    for i in np.arange(-2, 4, 0.5):
        fx = f.evalf(subs={x: i})
        mtz_i = np.append(mtz_i, i)
        mtz_fx = np.append(mtz_fx, fx)
        lst.append(fx)


    var_i = pd.Series(mtz_i, name="n")
    var_fx = pd.Series(mtz_fx, name="fx")

    tabla = pd.concat([var_i, var_fx], axis=1)
    print(tabla)
