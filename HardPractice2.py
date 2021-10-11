from decimal import Decimal

def check_constraint(person1: (int, int), person2: (int, int)):
    if person2[1] > person1[1] and person2[0] > person1[0]:
        return True
    return False


#input_list = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
input_list = [[1,1],[1,7],[1,9],[2,2],[2,6],[3,3],[3,5],[4,4]]
sorted_by_height = sorted(input_list, key=lambda item: item[0])
sorted_by_weight = sorted(input_list, key=lambda item: item[1])

result = []

for i in range(len(input_list)):
    person = sorted_by_height[i]
    if len(result) == 0:
        result.append(person)
    else:
        person_under = result[-1]
        if check_constraint(person_under, person):
            result.append(person)
        else:
            person = sorted_by_weight[i]
            if check_constraint(person_under, person):
                result.append(person)

print(result)

# aa = []
# for item in input_list:
#     ratio = Decimal(item[0] / item[1])
#     ratio = float(round(ratio, 3))
#     aa.append((item[0], item[1], ratio))
#
# aa.sort(key=lambda item: item[2])
# print(aa)
