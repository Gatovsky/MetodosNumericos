import numpy as np


def cramer(A, b, n):
    A_det = np.linalg.det(A)
    x = np.random.rand(n)

    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = b
        Di = np.linalg.det(Ai)
        x[i] = np.dot(Di, (1/A_det))

    return x


def main():
    M = np.array([[2, -1, -2],
                 [-1, 1, 1],
                 [1, -2, 1]])

    b = np.array([-2, 0, 8])

    vector = cramer(M, b, 3)
    print("\nx: {}\ny: {}\nz: {}".format(vector[0], vector[1], vector[2]))


if __name__ == '__main__':
    main()
