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

    B = np.array([
        [0.1, -0.6, 1, -1],
        [-2, 0.3, -4, 0.1],
        [1, 0.5, 0.1, -0.3],
        [0.5, -0.3, 0.6, 0.7]
    ], dtype='float64')

    b2 = np.array([1, 0, 1, 1])

    vector = cramer(B, b2, 4)
    print("\nx1: {}\nx2: {}\nx3: {}\nx4: {}".format(vector[0], vector[1], vector[2], vector[3]))


if __name__ == '__main__':
    main()
