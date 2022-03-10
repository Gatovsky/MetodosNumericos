from random import randint
import time


def main():
    repeat_rolling = True

    print("Hola, Bienvenido al casino. ¿Apuestas?")
    time.sleep(3)

    while repeat_rolling:
        print("Lanzando dados....")
        time.sleep(2)
        print("dado #1: ", randint(1, 6), "\ndado #2: ", randint(1, 6))
        print("Continuar lanzando?")

        repeat_rolling = ("s" or "si") in input().lower()

    print("\nadiós")


if __name__ == '__main__':
    main()
