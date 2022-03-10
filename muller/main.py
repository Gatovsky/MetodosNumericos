import grafica
import cambios_signo
import muller


def main():
    cambios_signo.cambios_signo()
    x2_1 = muller.muller(-1, -0.5, 1e-9)
    x2_2 = muller.muller(0, 0.5, 1e-9)
    x2_3 = muller.muller(2, 2.5, 1e-9)
    grafica.grafica(x2_1, x2_2, x2_3)

if __name__ == '__main__':
    main()
