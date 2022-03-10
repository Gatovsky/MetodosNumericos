"""
Utilice aritmética de 5 dígitos con corte para determinar las
raíces de la ecuación siguiente, por medio de las ecuaciones (3.12)
y (3.13).   x²– 5000.002x + 10

Nota: "{:.5f}".format(valor) denota un corte de 5 dígitos
"""
import math
from prettytable import PrettyTable


def main():
    table = PrettyTable()
    table2 = PrettyTable()
    a = 1.; b = -5000.002; c = 10.

    raiz = math.sqrt(math.pow(b, 2) - 4 * (a * c))

    x1aprox = (-b + raiz) / (2 * a)
    x2aprox = (-b - raiz) / (2 * a)
    x1r = -2. * c / (b + raiz)
    x2r = -2. * c / (b - raiz)

    eax1 = abs(x1r - x1aprox)
    erx1 = abs(eax1/x1r)
    erpx1 = erx1 * 100

    eax2 = abs(x2r - x2aprox)
    erx2 = abs(eax2 / x2r)
    erpx2 = erx2 * 100

    table.field_names = ["x1 aprox.", "x1 real", "error abs", "error relat.", "error r %"]
    table.add_row([x1aprox, x1r, eax1, erx1, erpx1])

    table2.field_names = ["x2 aprox.", "x2 real", "error abs", "error relat.", "error r %"]
    table2.add_row([x2aprox, x2r, eax2, erx2, erpx2])

    print(table)
    print("\n")
    print(table2)


if __name__ == '__main__':
    main()
