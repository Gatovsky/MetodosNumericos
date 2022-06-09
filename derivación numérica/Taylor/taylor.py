import math
import sympy as sp


def Taylor(a, n):
    x = sp.symbols('x')
    f = x**3 - 2 * x**2 - x + 1
    F = f
    T = f.subs(x, a)

    for k in range(1, n + 1):
        derivadafk = sp.diff(f, x)
        T = T + derivadafk.subs(x, a) * ((x - a)**k) / math.factorial(k)
        f = derivadafk

    print(sp.expand(T))

    grafica = sp.plot(F, T, (x, a - 3, a + 3), tittle='Serie de Taylor', show=False)
    grafica[0].line_color = 'dodgerblue'
    grafica[1].line_color = 'firebrick'
    grafica.show()
    grafica.save("taylor.png")


def main():
    a = 1  # valor de búsqueda alrededor
    n = 3  # grados de la función

    Taylor(a, n)


if __name__ == '__main__':
    main()
