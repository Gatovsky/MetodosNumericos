from prettytable import PrettyTable


def decimal2binario(binario, longitud):
    decimal = 0
    for b in range(len(binario)):
        longitud -= 1
        decimal += int(binario[b]) * pow(2, longitud)

    return decimal


def decimal2binario_punto(binario):
    decimal = 0
    punto = 0

    for i in range(len(binario)):
        if binario[i] == '.':
            break
        punto += 1

    binarios_izquierda = binario[:punto]
    binarios_derecha = binario[punto + 1:]
    lon_izquierda = len(binarios_izquierda)
    lon_derecha = 0

    for b in range(len(binarios_izquierda)):
        lon_izquierda -= 1
        decimal += int(binarios_izquierda[b]) * pow(2, lon_izquierda)

    for c in range(len(binarios_derecha)):
        lon_derecha += 1
        decimal += int(binarios_derecha[c]) * pow(2, lon_derecha*-1)   # multiplicar lon_derecha*-1 para ser negativo

    return decimal


def main():
    lst_decimales = list()
    lst_binarios = list()

    cantidad = int(input("Cantidad de binarios: "))

    while cantidad > 0:
        binario = input("binario: ")
        lst_binarios.append(binario)
        lon = len(binario)

        if binario.__contains__('.'):
            lst_decimales.append(decimal2binario_punto(binario))
        else:
            lst_decimales.append(decimal2binario(binario, lon))

        cantidad -= 1

    x = PrettyTable()
    x.field_names = ["Binario", "Decimal"]

    print("\n")

    for bina, dec in zip(lst_binarios, lst_decimales):
        x.add_row([bina, dec])

    print(x)


if __name__ == '__main__':
    main()
