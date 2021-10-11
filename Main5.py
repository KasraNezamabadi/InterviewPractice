# input = a[start ... mid ... end], key
# if: a[start] < a[mid] -> a[start ... mid] is sorted;
#    if key > a[start] & key < a[mid] -> recursive a[start...mid], key
#    else: recursive a[mid...end], key
# else: a[mid ... end] is sorted


def search_rotated(input_list: [int], start: int, end: int, key: int):
    mid = (start + end) // 2

    if input_list[mid] == key:
        print(mid)
        return mid

    if input_list[start] < input_list[mid]:  # a[start ... mid] is sorted

        if key < input_list[mid] and key > input_list[start]:
            return search_rotated(input_list, start, mid - 1, key)
        else:
            return search_rotated(input_list, mid + 1, end, key)

    else:  # a[mid ... end] is sorted
        if key > input_list[mid] and key < input_list[end]:
            return search_rotated(input_list, mid + 1, end, key)
        else:
            return search_rotated(input_list, start, mid - 1, key)


input_list = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
index = search_rotated(input_list, 0, len(input_list) - 1, 5)
print(index)