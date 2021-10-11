# The longest common subsequence in Python

def lcs_algo(S1, S2):

    # DP table L[i][j]: length of LCS upto ith and jth chars of first and second sequences.
    # Initializing L of size (|S1| + 1) x (|S2| + 1)
    temp = [0] * (len(S2) + 1)
    L = [temp] * (len(S1) + 1)

    # DP rule to update
    for i in range(len(S1) + 1):
        for j in range(len(S2) + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i - 1] == S2[j - 1]:  # Match! Increment L[i][j]
                L[i][j] = L[i - 1][j - 1] + 1
            else:  # No match! Use previous best
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    lcs_length = L[len(S1)][len(S2)]

    # Backtrack
    lcs_trace = [""] * (lcs_length + 1)
    lcs_trace[lcs_length] = ""

    i = len(S1)
    j = len(S2)
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs_trace[lcs_length - 1] = S1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS: " + "".join(lcs_trace))


S1 = "ACADB"
S2 = "CBDA"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2)

