def cutRod(price, n):
    val = [0 for x in range(n + 1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n + 1):
        max_val = -1
        for j in range(i):
            max_val = max(max_val, price[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]

