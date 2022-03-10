"""
escriba un programa
corto para determinar el número más pequeño, xmin
"""
import sys
from prettytable import PrettyTable


def main():
    t = PrettyTable()
    t.field_names = ["xmin con datos de Py_ssize_t", "xmin con un número x"]
    minimum = sys.maxsize          # mayor número soportado en python
    minimum = minimum.__float__()  # definido como punto flotante presición simple
    minn = 1.                      # número x de prueba

    # proceso usando los datos de Py_ssize_t
    while minimum + 1. > 1.:
        if minimum <= 0:
            break
        minimum /= 2.

    # proceso con un número x
    while minn + 1. > 1.:
        if minn <= 0:
            break
        minn /= 2

    t.add_row([minimum, minn])
    print(t)


if __name__ == '__main__':
    main()
