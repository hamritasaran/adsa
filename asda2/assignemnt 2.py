def matrix(matrices):
    n = len(matrices)
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + matrices[i - 1][0] * matrices[k][1] * matrices[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    def parenthesization(s, i, j):
        if i == j:
            return "A" + str(i)
        else:
            return "(" + parenthesization(s, i, s[i][j]) + \
                   "*" + parenthesization(s, s[i][j] + 1, j) + ")"

    optimal_parenthesization = parenthesization(s, 1, n - 1)
    return optimal_parenthesization, m[1][n - 1]
matrices = [(2, 3), (3, 4), (4, 2)]
optimal_parenthesization, min_scalar_multiplications = matrix(matrices)
print("Optimal Parenthesization:", optimal_ parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)
