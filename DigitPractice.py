
def count_2s(a: int):
    digits = []
    result = 0
    while a > 0:
        digits.append(a % 10)
        a = int(a/10)

    for digit in digits:
        if digit == 2:
            result += 1
    return result


name = ('kasra', 27)
print(name[1])

# names: [(str, int)]
#
# def count_previous_2s(a: int):
#     for i in range(a):
#         if count_2s(i) > 0:
#             print(i)

#digits = count_2s(12)

#count_previous_2s(25)

#print(digits)