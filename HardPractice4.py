
def find_shortest_dist(input_list: [str], word1: str, word2: str):

    word1_last_loc = -1
    word2_last_loc = -1
    min_distance = len(input_list)
    locs = ()

    for i in range(len(input_list)):

        word = input_list[i]

        if word == word1:
            word1_last_loc = i
        elif word == word2:
            word2_last_loc = i

    if word1_last_loc > -1 and word2_last_loc > -1:
        dist = abs(word1_last_loc - word2_last_loc)
        if dist < min_distance:
            min_distance = dist
            locs = (word1_last_loc, word2_last_loc)

    return locs[0], locs[1], min_distance


input_list = ['a', 'b', 'c', 'd', 'e', 'f', 'a']

print(find_shortest_dist(input_list, 'a', 'e'))

