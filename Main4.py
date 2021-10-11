def sort_anagrams(input_list: [str]):
    my_dict = {}

    for word in input_list:

        existing_keys = my_dict.keys()

        anagram_found = False

        for key in existing_keys:
            if is_anagram(word, key):
                my_dict[key].append(word)
                anagram_found = True
                break

        if not anagram_found:
            my_dict[word] = [word]

    result = []
    for key, value in my_dict.items():
        result.extend(value)

    print(result)


def is_anagram(str1: str, str2: str):
    if len(str1) == len(str2):

        str1_ascii = 0
        str2_ascii = 0

        for letter in str1.lower():
            str1_ascii += ord(letter)

        for letter in str2.lower():
            str2_ascii += ord(letter)

        if str1_ascii == str2_ascii:
            return True

    return False


input_list = ['abcd', 'acb', 'ab', 'acdb', 'dcba', 'bca', 'ba']
sort_anagrams(input_list)













