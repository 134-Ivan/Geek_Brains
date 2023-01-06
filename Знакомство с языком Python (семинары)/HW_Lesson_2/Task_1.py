# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('введите вещественное число: ')

num_list = []
for i in number:
    if i.isdigit():
        num_list.append(int(i))

sum_numbers = sum(num_list)

print(sum_numbers)
