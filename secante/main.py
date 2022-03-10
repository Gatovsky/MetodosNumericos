import math

import sympy as sp
import grafica
import secante
import secante_modificada

def main():
    e = math.e
    x = sp.symbols('x')
    # f = e**(-x**2) - x
    f = e**(-x**2) -x
    # x3 = secante.secante(f,x, 0, 1, 0.1)
    x3 = secante_modificada.secante_modif(f, x, 1, 0.01, 1e-7)
    grafica.grafica(x3)

    print(max(1e7, 1e-7))


if __name__ == '__main__':
    main()