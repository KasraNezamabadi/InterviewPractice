

def lis(input_list):
    # DP table L[i]: length of LIS upto ith element. Answer: max(L)
    # Initializing L of size |input_list|
    L = [1] * len(input_list)

    # L[i] = max(L[j]) for 0 <= j < i and arr[j] < arr[i]
    for i in range(1, len(input_list)):
        for j in range(0, i):
            if input_list[i] > input_list[j] and L[i] < L[j] + 1:
                L[i] = L[j] + 1

    index = L.index(max(L))
    result = []
    while index >= 0 and max(L) > 0:
        result.append(input_list[index])
        temp = max(L)
        for i in range(len(L)):
            if L[i] == temp:
                L[i] = -1
        index = L.index(max(L))

    result.reverse()
    return result


# end of lis function

# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", lis(arr))