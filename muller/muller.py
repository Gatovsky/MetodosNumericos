import sympy as sp
import pandas as pd
import numpy as np

def muller(x0, x1, ae):
    x = sp.symbols('x')
    f = x**5 -3.5 * x**4 + 2.75 * x**3 + 2.125* x**2 - 3.875 * x + 1.2
    x2 = (x0 + x1) / 2

    m_x0 = np.array([])
    m_x1 = np.array([])
    m_x2 = np.array([])
    m_x3 = np.array([])
    m_fx0 = np.array([])
    m_fx1 = np.array([])
    m_fx2 = np.array([])
    m_fx3 = np.array([])
    m_h0 = np.array([])
    m_h1 = np.array([])
    m_d0 = np.array([])
    m_d1 = np.array([])
    m_a = np.array([])
    m_b = np.array([])
    m_c = np.array([])


    while True:
        fx0 = f.evalf(subs={x: x0})
        fx1 = f.evalf(subs={x: x1})
        fx2 = f.evalf(subs={x: x2})

        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (fx1 - fx0) / h0
        d1 = (fx2 - fx1) / h1

        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = fx2

        if b < 0:
            x3 = x2 - ((2 * c) / (b - (sp.sqrt(b**2 - 4 * (a * c)))))
        else:
            x3 = x2 - ((2 * c) / (b + (sp.sqrt(b**2 - 4 * (a * c)))))

        fx3 = f.evalf(subs={x: x3})

        x0 = x1
        x1 = x2
        x2 = x3

        m_x0 = np.append(m_x0, x0)
        m_x1 = np.append(m_x1, x1)
        m_x2 = np.append(m_x2, x2)
        m_x3 = np.append(m_x3, x3)
        m_fx0 = np.append(m_fx0, fx0)
        m_fx1 = np.append(m_fx1, fx1)
        m_fx2 = np.append(m_fx2, fx2)
        m_fx3 = np.append(m_fx3, fx3)
        m_h0 = np.append(m_h0, h0)
        m_h1 = np.append(m_h1, h1)
        m_d0 = np.append(m_d0, d0)
        m_d1 = np.append(m_d1, d1)
        m_a = np.append(m_a, a)
        m_b = np.append(m_b, b)
        m_c = np.append(m_c, c)

        if fx3 <= ae:
            break


    var_x0 = pd.Series(m_x0, name="x0")
    var_x1 = pd.Series(m_x1, name="x1")
    var_x2 = pd.Series(m_x2, name="x2")
    var_x3 = pd.Series(m_x3, name="x3")
    var_fx0 = pd.Series(m_fx0, name="f(x0)")
    var_fx1 = pd.Series(m_fx1, name="f(x1)")
    var_fx2 = pd.Series(m_fx2, name="f(x2)")
    var_fx3 = pd.Series(m_fx3, name="f(x3)")
    var_ho = pd.Series(m_h0, name="h0")
    var_h1 = pd.Series(m_h1, name="h1")
    var_d0 = pd.Series(m_d0, name="d0")
    var_d1 = pd.Series(m_d1, name="d1")
    var_a = pd.Series(m_a, name="a")
    var_b = pd.Series(m_b, name="b")
    var_c = pd.Series(m_c, name="c")

    tabla = pd.concat([var_x2, var_b, var_fx3], axis=1)

    print(tabla)
    print("raíz: {0:.4f}".format(x2))

    return x2
