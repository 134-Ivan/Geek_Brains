# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers = [2, 3, 5, 9, 3]

def odd_number (list_of_numbers):
    sum_odd_numbers = 0
    dict_of_numbers = dict(enumerate(list_of_numbers))
    for key, value in dict_of_numbers.items():
        if key%2 == 0:
            continue
        else:
            sum_odd_numbers += value

    return sum_odd_numbers

print(odd_number(numbers))
