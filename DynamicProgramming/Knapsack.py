def knapSack(W, weigts, values):

    n = len(values)
    D = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):

            if i == 0 or j == 0:
                D[i][j] = 0

            elif weigts[i - 1] <= j:
                D[i][j] = max(values[i-1] + D[i-1][j - weigts[i - 1]], D[i-1][j])

            else:
                D[i][j] = D[i-1][j]

    return D[n][W]


values = [50, 100, 150, 200]
weights = [8, 16, 32, 40]
W = 64

print(knapSack(W, weights, values))