import numpy as np

def simplex_method(c, A, b):
    m, n = A.shape
    tableau = np.hstack((A, np.eye(m)))
    c = np.concatenate((c, np.zeros(m)))

    while True:
        j = np.argmin(c)
        if c[j] >= 0:
            break

        ratios = b / tableau[:, j]
        i = np.argmin(ratios)

        pivot = tableau[i, j]
        tableau[i, :] /= pivot
        for k in range(m):
            if k != i:
                tableau[k, :] -= tableau[k, j] * tableau[i, :]

        c -= c[j] * tableau[i, :]

    x = tableau[:, -m:]
    f = -c[-m:]

    return x, f

# Пример задачи:
c = np.array([-1, -2])
A = np.array([[1, 2, 8, 4], [3, 3, 5, 7], [4, 2, 1, 5], [8, 5, 1, 2]])
b = np.array([6, 12, 5, 2])

x, f = simplex_method(c, A, b)
print(f"Оптимальное решение: x = {x}, f = {-f}")
