import numpy as np
import pandas as pd


def secante_modif(f, x, x1, delta, ae):
    n = 0
    mtz_n = np.array([])
    mtz_x2 = np.array([])
    mtz_err = np.array([])

    while True:
        print("while")
        x2 = x1 - (delta * x1) * f.evalf(subs={x: x1}) / (f.evalf(subs={x: x1 + (delta*x1)}) - f.evalf(subs={x: x1}))
        x1 = x2

        err = abs(f.evalf(subs={x: x2}))
        n += 1

        mtz_n = np.append(mtz_n, n)
        mtz_x2 = np.append(mtz_x2, x2)
        mtz_err = np.append(mtz_err, err)

        if err < ae:
            break

    var_n = pd.Series(mtz_n, name="n")
    var_x2 = pd.Series(mtz_x2, name="x2")
    var_err = pd.Series(mtz_err, name="err")

    table = pd.concat([var_n, var_x2, var_err], axis=1)

    print(table)
    return x2
