# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random

example_list = [1, 2, 3, 4, 5, 6]

def mix(any_list):
    random_list = []
    l = 1
    while l <= len(any_list):
        i = random.choice(any_list)
        if i in random_list:
            continue
        else:
            random_list.append(i)
        l += 1

    print(random_list)

mix(example_list)
