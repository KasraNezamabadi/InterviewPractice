def edit_distance(str1, str2):

    rows = len(str1) + 1
    cols = len(str2) + 1
    D = [ [0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        D[i][0] = i

    for j in range(1, len(str2)+1):
        D[0][j] = j

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):

            insertion = D[i][j-1] + 1
            deletion = D[i-1][j] + 1
            match = D[i-1][j-1]
            if str1[i-1] != str2[j-1]:
                match += 1

            D[i][j] = min([insertion, deletion, match])

    return int(D[-1][-1])


a = edit_distance('abcd', 'acd')
print(a)

