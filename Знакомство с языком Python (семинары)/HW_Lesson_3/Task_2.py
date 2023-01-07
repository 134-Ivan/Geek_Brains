# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

example_one = [2, 3, 4, 5, 6]
example_two = [2, 3, 5, 6]
example_three = [7]

def multi(list_of_numbers):
    copy_list = list_of_numbers[:]
    list_of_multi = []
    while len(copy_list) > 1:
        list_of_multi.append(copy_list[0]*copy_list[-1])
        del copy_list[0], copy_list[-1]
    else:
        if len(copy_list) == 1:
            list_of_multi.append(copy_list[0]**2)
        else:
            pass

    return (list_of_multi)

print(f'первый пример {multi(example_one)}')
print(f'второй пример {multi(example_two)}')
print(f'третий пример {multi(example_three)}')
