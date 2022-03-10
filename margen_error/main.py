import math
import matplotlib.pyplot as plt


def entrada_datos():
    a = float(input("a: "))
    b = float(input("b: "))
    ter = int(input("término de la serie: "))

    return [a + b, ter]


def grafica_margen_error(lst_margen, lstx):
    fig, ax = plt.subplots()
    ax.plot(lstx, lst_margen, color='tab:orange', marker='o')
    ax.set_title('Error Relativo', loc="center",
                 fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
    ax.set_xlabel('Número de términos', loc='center', fontdict={'fontsize': 10,
                                                                'fontweight': 'bold', 'color': 'tab:blue'})
    ax.set_ylabel('', loc='center', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.show()


def grafica_grados_confianza(lst_grd, lstx):
    fig, ax = plt.subplots()
    ax.plot(lstx, lst_grd, color='tab:green', marker='o')
    ax.set_title('Grados de Confianza', loc="center",
                 fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
    ax.set_xlabel('Número de términos', loc='center', fontdict={'fontsize': 10,
                                                                'fontweight': 'bold', 'color': 'tab:blue'})
    ax.set_ylabel('', loc='center', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    plt.show()


def merge_graficas(lst_margen, lst_grd, lstx):
    fig, ax = plt.subplots()
    ax.plot(lstx, lst_margen, color='tab:orange', marker='o')
    ax.plot(lstx, lst_grd, color='tab:blue', marker='o')

    ax.set_title('Comparación de Gráficas', loc="center",
                 fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': 'tab:blue'})
    ax.set_xlabel('Número de términos', loc='center', fontdict={'fontsize': 10,
                                                                'fontweight': 'bold', 'color': 'tab:blue'})
    ax.set_ylabel('', loc='center', fontdict={'fontsize': 10, 'fontweight': 'bold', 'color': 'tab:blue'})
    ax.legend(['margen error', 'grados confianza'])
    plt.show()


def main():
    datos = entrada_datos()
    xi = 0
    lst_errs_absoluto = list()
    lst_errs_relativo = list()
    lst_grd_cofianza = list()
    lst_ejex = list()

    x = datos[0]   # valor real dado por a+b
    k = datos[1]   # k-términos para la sumatoria

    for i in range(k):
        xi += 1 / math.factorial(i)   # sumatoria 1/k!
        err_a = abs(x - xi)           # error absoluto |x - xi|
        err_r = abs(err_a / x)        # error relativo |x - xi /x|
        grd_confianza = abs(1-err_r)  # grados de confianza |1 - error relativo|

        lst_errs_absoluto.append(err_a)
        lst_errs_relativo.append(err_r)
        lst_grd_cofianza.append(grd_confianza)
        lst_ejex.append(i+1)

    print("############# Margen de error ##############\n")
    for err1, err2 in zip(lst_errs_absoluto, lst_errs_relativo):
        print("Margen de error cuando xi={} ---> {}".format(round(err1, 5), round(err2*100, 2)), "%")

    print("\n############# Grados de confianza ##############\n")
    for err_relat, grd in zip(lst_errs_relativo, lst_grd_cofianza):
        print("Cuando el margen de error es de {}% existe un {}% de confianza".format(round(err_relat*100, 2), round(grd*100, 2)))

    grafica_margen_error(lst_errs_relativo, lst_ejex)
    grafica_grados_confianza(lst_grd_cofianza, lst_ejex)
    merge_graficas(lst_errs_relativo, lst_grd_cofianza, lst_ejex)


if __name__ == '__main__':
    main()
