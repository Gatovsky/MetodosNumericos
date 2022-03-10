import sympy as sp


def division_sintetica(a, residuo):
    a = list(reversed(a))
    lon = len(a)
    b = [0.0] * lon
    b[lon-1] = a[lon-1]

    i = lon - 2

    while i >= 0:
        b[i] = a[i] + (residuo * b[i+1])
        i -= 1
    return list(reversed(b))


def main():
    x = sp.symbols('x')
    denominador = x - 0.5 * x - (-1)
    g = sp.solve(denominador)
    polinomio = ""

    b = division_sintetica([1, -3.5, 2.75, 2.125, -3.875, 1.25], g[0])
    print("\nResiduo: {}".format(str(b[b.__len__()-1])))
    print("\nCoeficientes: {}".format(b[: b.__len__()-1]))

    # concatenamos los valores del arreglo
    for i in range(0, b.__len__()-1):
        polinomio += str(b[i])+"x^"+str(b.__len__()-2-i)+" "

    # se imprime el polinomio y
    # sí el residuo es diferente de 0 se anexa la fiferencia
    if b[b.__len__()-1] != 0:
        print(polinomio+str(b[b.__len__()-1])+"/"+str(denominador))
    else:
        print(polinomio)


if __name__ == '__main__':
    main()
