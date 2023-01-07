# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo_list(number):
    list_of_numbers = [1, 0, 1]

    for i in range(number-1):
        list_of_numbers.append(list_of_numbers[-1]+list_of_numbers[-2])
        list_of_numbers.insert(0, (list_of_numbers[1]-list_of_numbers[0]))

    print(list_of_numbers)

fibo_list(8)
