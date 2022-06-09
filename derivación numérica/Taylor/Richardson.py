from math import *


def pol(x):
    return x**3 - 2 * x**2 - x + 1


def trig(x):
    return x * cos(x - 1) - sin(x)


def dercentrada(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def richardson(f, x, h):
    d = (3 / 2) * dercentrada(f, x, h / 2) - (1 / 2) * dercentrada(f, x, h)

    return d


def main():
    x = 1
    h = 0.1

    print("{0:.12f}".format(richardson(pol, x, h)))
    # print("{0:.12f}".format(richardson(trig, x, h)))


if __name__ == '__main__':
    main()
