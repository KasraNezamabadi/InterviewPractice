
# [2 * 3 + 5 / 6 * 3 + 15]
# i = 0 -> op1 = 2
# i = 1 -> op2 = 3, t = 6, del 0, del 0, del 0, insert(0, t)
# i = 1

def cal_equation(equation):


    i = 0
    operand_1 = 0
    operand_2 = 0

    while i < len(equation):

        item = equation[i]

        if item == '*':

            operand_2 = equation[ i +1]
            print('OP1: ' + str(operand_1), 'OP2: ' + str(operand_2))
            temp_result = operand_1 * operand_2
            print(temp_result)
            del equation[ i -1]
            del equation[ i -1]
            del equation[ i -1]
            equation.insert( i -1, temp_result)
            operand_1 = temp_result

        elif item == '/':

            operand_2 = equation[ i +1]
            temp_result = operand_1 / operand_2
            del equation[ i -1]
            del equation[ i -1]
            del equation[ i -1]
            equation.insert( i -1, temp_result)
            operand_1 = temp_result

        elif item == '+' or item == '-':
            i += 1
        else:
            operand_1 = item
            i += 1


    result = 0
    i = 0

    while i < len(equation):

        item = equation[i]

        if item == '+':
            operand_2 = equation[ i +1]
            result = operand_1 + operand_2
            operand_1 = result
            i += 2

        elif item == '-':

            operand_2 = equation[ i +1]
            result += operand_1 - operand_2
            operand_1 = result
            i += 2

        else:
            operand_1 = item
            i += 1


    print(result)


equation = [2, '*', 3, '+', 5, '/', 6, '*', 3, '+', 15]
cal_equation(equation)