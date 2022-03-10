import numpy as np
import pandas as pd


def secante(f, x, x1, x2, ae):
    n = 0
    err = 0
    x3 = 0

    mtz_n = np.array([])
    mtz_x3 = np.array([])
    mtz_err = np.array([])

    while True:
        x3 = x1 - ((x2 - x1) / (f.evalf(subs={x: x2}) - f.evalf(subs={x: x1}))) * f.evalf(subs={x: x1})
        x1 = x2
        x2 = x3

        err = abs(f.evalf(subs={x: x3}))
        print(err)
        n += 1

        mtz_n = np.append(mtz_n, n)
        mtz_x3 = np.append(mtz_x3, x3)
        mtz_err = np.append(mtz_err, err)

        if err <= ae:
            break

    var_n = pd.Series(mtz_n, name="n")
    var_x3 = pd.Series(mtz_x3, name="x3")
    var_err = pd.Series(mtz_err, name="err")

    table = pd.concat([var_n, var_x3, var_err], axis=1)


    print(table)

    return  x3

