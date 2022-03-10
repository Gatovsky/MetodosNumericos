import cmath
import random
import grafica


def bairstow():
    a = [3, 0, 0, 0, 0, 0]
    # x = sympy.symbols('x')
    # f = x**5 - 3.5 * x**4 + 2.75 * x**3 + 2.125 * x**2 - 3.875 * x + 1.25


    r = -1
    s = -1
    b0 = random.random()
    b1 = random.random()
    b2 = random.random()
    b3 = random.random()
    b4 = random.random()
    b5 = random.random()

    while abs(b0 > 0.0001) or abs(b1 > 0.0001):
        b5 = a[0]
        b4 = (b5 * r) + a[1]
        b3 = (b4 * r) + (b5 * s) + a[2]
        b2 = (b3 * r) + (b4 * s) + a[3]
        b1 = (b2 * r) + (b3 * s) + a[4]
        b0 = (b1 * r) + (b2 * s) + a[5]

        c5 = b5
        c4 = (c5 * r) + b4
        c3 = (c4 * r) + (c5 * s) + b3
        c2 = (c3 * r) + (c4 * s) + b2
        c1 = (c2 * r) + (c3 * s) + b1

        # incremento / determinante
        dr = (((-b1) * (c2)) - ((-b0) * (c3))) / ((c2**2) - (c1 * c3))
        ds = (((c2) * (-b0)) - ((c1) * (-b1))) / ((c2**2) - (c1 * c3))

        r = dr + r
        s = ds + s
    p = (-r)
    q = (-s)

    # Raíces
    r1 = (-b3 + cmath.sqrt((b3**2.) - 4. * b4 * b2)) / (2. * b4)
    r2 = (-b3 - cmath.sqrt((b3**2.) - 4. * b4 * b2)) / (2. * b4)
    r3 = (-p + cmath.sqrt((p**2.) - 4. * a[0] * q)) / (2. * a[0])
    r4 = (-p - cmath.sqrt((p**2.) - 4. * a[0] * q)) / (2. * a[0])
    r5 = (s / r)

    return r1, r2, r3, r4


def main():
    a = bairstow()
    for i in a:
        print("{0:.4f}".format(i))

    grafica.grafica(a)


if __name__ == '__main__':
    main()
