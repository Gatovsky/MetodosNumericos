import numpy as np


# fórmula: λ_(i+1) * x_(i+1) = Ax_i
# Mayor valor característico
def p_maxValor(A, x0, eps=1e-12, n=500):
    print()

    xi = x0
    λ = 0
    for i in range(n):
        x_anterior = xi
        λ_anterior = λ

        Ax = np.dot(A, xi)
        # Ordenar por valor absoluto
        Ax_order = np.sort(abs(Ax))
        λ = Ax_order[-1]
        xi = np.dot(Ax, (1/λ))

        if np.linalg.norm(abs(λ - λ_anterior)) < eps:
            return xi, λ
    return xi, λ


# Menor valor característico
# fórmula: (1/λ)x = A⁻¹x
def p_minValor(A, x0, eps=1e-12, n=500):
    A_inv = np.linalg.inv(A)

    xi = x0
    λ = 0
    for i in range(n):
        x_anterior = xi
        λ_anterior = λ

        A_invx = np.dot(A_inv, xi)
        # ordenar por mayor absoluto
        A_invx_order = np.sort(abs(A_invx))
        λ = A_invx_order[-1]
        xi = np.dot(A_invx, (1/λ))

        if np.linalg.norm(abs(λ - λ_anterior)) < eps:
            return xi, λ
    return xi, λ


def main():
    matriz = np.array([
        [3.556, -1.778, 0],
        [-1.778, 3.556, -1.778],
        [0, -1.778, 3.556]
    ])
    x0 = np.array([1, 0, 1])

    lst =p_maxValor(matriz, x0, 1e-12)
    lst2 = p_minValor(matriz, x0, 1e-12)

    x = lst[0]
    λ = lst[1]
    x2 = lst2[0]
    λ2 = lst2[1]

    print("### Mayor valor característico ###\n")
    print("vector proporcional: [{:0.4f}, {:0.4f}, {:0.4f}]".format(x[0], x[1], x[2]))
    print("λ máxima: {:0.4f}".format(λ))
    print("\n### Menor valor característico ###\n")
    print("vector proporcional: [{:0.4f}, {:0.4f}, {:0.4f}]".format(x2[0], x2[1], x2[2]))
    print("λ mínima: {:0.4f}".format(λ2))


if __name__ == '__main__':
    main()
