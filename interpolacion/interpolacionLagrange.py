import numpy as np
import sympy as sp
from grafica import grafica


def interpolacionLagrange(xi, fi):
    n = len(xi)
    x = sp.Symbol('x')
    polinomio = 0

    for i in range(0, n, 1):
        numerador = 1
        denominador = 1

        for j in range(0, n, 1):
            if i != j:
                numerador = numerador * (x - xi[j])
                denominador = denominador * (xi[i] - xi[j])
            termino = (numerador / denominador) * fi[i]
        polinomio += termino

    polinomioSimple = sp.expand(polinomio)
    px = sp.lambdify(x, polinomio)

    muestras = 250
    a = np.min(xi)
    b = np.max(xi)
    p_xi = np.linspace(a, b, muestras)
    p_fi = px(p_xi)

    print(p_xi, p_fi)

    grafica(xi, fi, p_xi, p_fi, polinomioSimple)

    print("\n polinomio= \n", polinomio)
    print("\nPolinomio simplifcado= \n", polinomioSimple)



def main():
    interpolacionLagrange(np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]), np.array([0, 2.12, 3.02, 3.25, 3.14, 2.85, 2.51, 2.16, 1.84]))


if __name__ == '__main__':
    main()
