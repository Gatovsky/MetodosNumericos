"""
Calcule la memoria de acceso al azar (RAM) en megabytes, que es necesaria para almacenar un
arreglo multidimensional de 20 × 40 × 120. Este arreglo es de doble precisión, y cada valor
requiere una palabra de 64 bits. Recuerde que una palabra de 64 bits = 8 bytes, y un kilobyte = 210
bytes. Suponga que el índice
"""


def main():
    arreglo = [[20.], [40.], [120.]]
    arreglo_t = arreglo[0][0] * arreglo[1][0] * arreglo[2][0]

    print("{} MB reservados para el arreglo".format(arreglo.__sizeof__()))
    print("{} MB ocupados por los datos del arreglo".format(arreglo_t.__sizeof__()))


if __name__ == '__main__':
    main()
