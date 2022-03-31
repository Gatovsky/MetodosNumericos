import numpy as np


def suma(A, B):
    C = A +B

    print("\nA + B = \n", C)


def resta(A, B):
    C = A - B

    print("\nA - B = \n", C)


def producto(A, B):
    C = np.dot(A, B)

    print("\nA · B = \n", C)


def div(A, B):
    C = A / B

    print("\nA / B = \n", C)

def inver(A, B):
    A_inv = np.linalg.inv(A)
    B_inv = np.linalg.inv(B)

    print("\nA⁻¹ = \n", A_inv)
    print("\nB⁻¹ = \n", B_inv)


def transpos(A, B):
    A_t = np.transpose(A)
    B_t = np.transpose(B)

    print("\nAᵀ= \n", A_t)
    print("\nBᵀ = \n", B_t)


def main():
    A = np.array([[1, -1, 3, 4],
                  [2, 4, 5, 3],
                  [3, 2, 1, 4],
                  [3, 2, -1, 5]], dtype='float64')

    B = np.array([[1, -1, 3, 4],
                  [2, 4, 5, 3],
                  [3, 2, 1, 4],
                  [3, 2, -1, 5]], dtype='float64')

    suma(A, B)
    resta(A, B)
    producto(A, B)
    div(A, B)
    inver(A, B)
    transpos(A, B)


if __name__ == '__main__':
    main()
