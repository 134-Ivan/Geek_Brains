# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('Введите число n: '))

list_of_numbers = []

for i in range(1, n+1):
    value = round(((1+1/i)**i), 2)
    list_of_numbers.append(value)

# Проверка вывода списка значений расчитанных по формуле
print(list_of_numbers)

# Подсчет суммы значений в полученном списке
sum_of_numbers = sum(list_of_numbers)
print(sum_of_numbers)