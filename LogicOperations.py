
def add_without_plus(a: int, b: int):

    # recursive (a XOR b, shift(a AND b))

    if b == 0:
        return a

    sum = a ^ b
    carry = (a & b) << 1
    return add_without_plus(sum, carry)


def subtract_without_minus(a: int, b: int):

    # recursive (a XOR b, shift(~a AND b))

    if b == 0:
        return a

    borrow = (~a) & b
    return subtract_without_minus(a ^ b, borrow << 1)


#print(add_without_plus(12, 17))

print(subtract_without_minus(17, 12))

