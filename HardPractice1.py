def calculate_similarity(dec_1: [int], doc_2: [int]):
    # sim = |A ^ B| / |A U B|

    set1 = set(dec_1)
    set2 = set(doc_2)

    set_intersect = set1 & set2
    set_union = set1 | set2

    sim = len(set_intersect) / len(set_union)

    return sim


input = {13: [14, 15, 100, 9, 3], 16: [32, 1, 9, 3, 5], 19: [15, 29, 2, 6, 8, 7], 24: [7, 10]}

result = {}
for key1, value1 in input.items():

    for key2, value2 in input.items():
        if key1 == key2:
            continue

        if len(value1) == 0 or len(value2) == 0:
            continue

        tup_key = (key1, key2)
        if key1 > key2:
            tup_key = (key2, key1)

        if tup_key in result:
            continue

        sim = calculate_similarity(value1, value2)

        if sim > 0:
            result[tup_key] = sim

final_result = dict(reversed(sorted(result.items(), key=lambda item: item[1])))

# print('ID1, ID2:    SIMILARITY')
# for key, value in final_result.items():
#     print(key, value)


my_list = [(1, 4, 2), (2, 3, 6), (7, 5, 9)]
my_list.sort(key=lambda item: item[2])
print(my_list)



















