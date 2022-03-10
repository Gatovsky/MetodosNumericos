'''determinar el épsilon de máquina de su computadora'''


def main():
    eps = 1
    while eps + 1 > 1:
        eps /= 2

    eps *= 2
    print(eps)


if __name__ == '__main__':
    main()
