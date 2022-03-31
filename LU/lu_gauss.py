import numpy as np
import scipy.linalg as sci


def factorizacionLU(A):
    P, L, U = sci.lu(A)

    print("A = \n", A)
    print("\nP = \n", P)
    print("\nL = \n", L)
    print("\nU = \n", U)
    print("\nA = LU\n", np.dot(L, U))
    if A.all() == (np.dot(L,U)).all():
        print("\n\nSe cumple que A = LU")


def determinante(A):
    detA = np.linalg.det(A)

    print(detA)


def main():
    A = np.array([[1, -1, 3, 4],
                  [2, 4, 5, 3],
                  [3, 2, 1, 4],
                  [3, 2, -1, 5]], dtype='float64')
    b = np.array([7.85, -19.5617, 71.4])

    factorizacionLU(A)

    determinante(A)


if __name__ == '__main__':
    main()
