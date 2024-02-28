def braun_robinson(matrix):
    col = len(matrix)
    row = len(matrix[0])

    # Initialize arbitrary strategies
    p = [1] + [0] * (row - 1)
    q = [1] + [0] * (col - 1)

    N = 1000  # Number of iterations
    count = 1
    FLAG_PRINT = True

    while True:
        max_alpha = [sum(matrix[j][i] * q[i] for i in range(col)) for j in range(row)]
        alpha = max(max_alpha)
        A = max_alpha.index(alpha)

        min_betta = [sum(matrix[j][i] * p[i] for i in range(row)) for j in range(col)]
        betta = min(min_betta)
        B = min_betta.index(betta)

        v = (alpha + betta) / 2

        if count == N:
            break

        p[A] = (count * p[A] + 1) / (count + 1)
        q[B] = (count * q[B] + 1) / (count + 1)

        if FLAG_PRINT:
            print("___________________")
            print(f"iter №{count}")
            print(f"alpha = {alpha}")
            print(f"betta = {betta}")
            print(f"v = {v}")
            print(f"p = {p}")
            print(f"q = {q}")
            print("___________________\n")

        count += 1

    print("\n******** Решение ********")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"v = {v}")

# Example usage:
matrix_example = [
    [1, 2, 8, 4],
    [3, 3, 5, 7],
    [4, 2, 1, 5],
    [8, 5, 1, 2]
]

braun_robinson(matrix_example)
