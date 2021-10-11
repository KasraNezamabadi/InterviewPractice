def find_majority(input_list: [int]):
    frequency_dict = {}
    max_frequency = 0
    majority_tup = ()

    for item in input_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1

        if max_frequency < frequency_dict[item]:
            max_frequency = frequency_dict[item]
            majority_tup = (item, frequency_dict[item])

    if majority_tup[1] >= int(len(input_list) / 2):
        return majority_tup
    return -1


input_list = [1, 2, 5, 9, 5, 9, 5, 5, 5]
print(find_majority(input_list))

