"""
Evalúe e–5 con el uso de dos métodos y compárelo con el valor verdadero de 6.737947 × 10–3. Utilice
20 términos para evaluar cada serie y calcule los errores relativos
aproximado y verdadero como términos que se agregaran.
"""
import math
from prettytable import PrettyTable



def M2():
    table2 = PrettyTable()
    table2.title = "Tabla del método 2"
    table2.field_names = ["n", "test...", "Et %", "Ea %"]
    x2 = -5 * -1

    e2 = math.exp(x2)
    Es2 = e2 * math.pow(10, 2 - 3)
    test2 = 1
    v_anterior = 1
    contador2 = 1

    Et2 = abs(((e2 - test2) / e2)) * 100
    Ea2 = 0
    table2.add_row([contador2, test2, Et2, Ea2])

    while contador2 < 20:
        test2 = test2 + math.pow(x2, contador2) / math.factorial(contador2)
        Et2 = abs(((e2 - test2) / e2)) * 100
        Ea2 = abs((test2 - v_anterior) / test2) * 100

        table2.add_row([contador2, test2, Et2, "{:.9f}".format(Ea2)])
        contador2 += 1
        v_anterior = test2

    print(table2)


def M1():
    table = PrettyTable()
    table.title = "Tabla del método 1"
    table.field_names = ["n", "test", "Et %", "Ea %"]
    x = -5
    e = math.exp(x)
    Es = e * math.pow(10, 2 - 3)
    v_anterior = 1
    contador = 1

    test = 1
    Et = abs(((e - test) / e)) * 100
    Ea = abs((test - v_anterior) / test) * 100
    table.add_row([contador, test, Et, Ea])

    while contador < 20:
        if contador % 2 == 0:
            test = test + math.pow(x, contador) / math.factorial(contador)
        else:
            test = test - math.pow(x, contador) / math.factorial(contador)

        Et = abs(((e - test) / e)) * 100
        Ea = abs((test - v_anterior) / test) * 100

        contador += 1
        v_anterior = test
        table.add_row([contador, test, Et, "{:.9f}".format(Ea)])

    print(table)


def main():
    M1()
    M2()


if __name__ == '__main__':
    main()
