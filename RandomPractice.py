import random as rnd


def shuffle(cards: [int]):

    for i in range(len(cards)):
        random_index = rnd.randint(0, i)
        cards[i], cards[random_index] = cards[random_index], cards[i]


def random_subset(input_list: [int], subset_size: int):
    subset = input_list[:subset_size]

    for i in range(subset_size, len(input_list)):
        random_index = rnd.randint(0, i)
        if random_index < subset_size:
            subset[random_index] = input_list[i]

    return subset


cards = [1, 2, 3, 4, 5, 6, 7, 8]

print(random_subset(cards, 5))
# shuffle(cards)
# print(cards)

