"""
Evalúe el polinomio y = x² - 7x² + 8x + 0.35 en x = 1.37. Utilice aritmética de 3 dígitos con corte.
Evalúe el error relativo porcentual. Repita el inciso a) pero exprese a y como y=[(x - 7)x + 8]x + 0.35
"""
from prettytable import PrettyTable


def main():
    x = 1.37
    t = PrettyTable()
    t2 = PrettyTable()

    y = pow(x, 3) - 7*pow(x, 2) + 8*x + 0.35
    y2 = ((x - 7) * x + 8) * x + 0.35

    error_abs = abs(x - y)
    error_rela = abs(error_abs/x)
    error_rela_percent = error_rela*100

    error_abs2 = abs(x - y2)
    error_rela2 = abs(error_abs2/x)
    error_rela_percent2 = error_rela2*100

    t.field_names=["polinomio", "x", "Error abs", "Error relativo", "Error r. porcent %"]
    t.add_row(["y=x² - 7x² + 8x + 0.35", x, "{:.3f}".format(error_abs), "{:.3f}".format(error_rela), "{:.3f}".format(error_rela_percent)])

    t2.field_names=["polinomio", "x", "Error abs", "Error relativo", "Error r. porcent %"]
    t2.add_row(["y=[(x - 7)x + 8]x + 0.35", x, "{:.3f}".format(error_abs2), "{:.3f}".format(error_rela2), "{:.3f}".format(error_rela_percent2)])
    print(t)
    print("\n")
    print(t2)


if __name__ == '__main__':
    main()
