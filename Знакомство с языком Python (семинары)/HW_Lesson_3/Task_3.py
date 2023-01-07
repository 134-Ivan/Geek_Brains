# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# (если получаются длинные числа после запятой, это нормально и
# особенность данного языка программирования. ваш ответ может не
# совпадать с примером(может получитя 0,20))
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

example_one = [1.1, 1.2, 3.1, 5, 10.01]
example_two = [1.5, 0.01]


def diffrence_finder(any_list):
    decimal_list = []
    for number in any_list:
        decimal_number = number-int(number)
        decimal_list.append(round(decimal_number, 2))

    diff = max(decimal_list) - min(decimal_list)
    return diff

print(diffrence_finder(example_one))
print(diffrence_finder(example_two))