# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

from random import randint

N = int(input('Введите число N: '))

# Формирование списка [-N, N]
list_of_numbers = []

for i in range (-N, N+1):
    list_of_numbers.append(i)

print(list_of_numbers)

# Создание рандомного списка с количеством значений N из сформированного списка [-N, N]
random_list = []

for j in range (1, N+1):
    random_list.append(randint(list_of_numbers[0], list_of_numbers[-1]))

print(random_list)

# Формула поиска произведения элементов на указанных позициях ПРОВЕРКУ НА ЗНАЧЕНИЕ ВЫХОДЯЩЕЕ ЗА ГРАНИЦЫ СПИСКА НЕ ПРОВОДИЛ
def multiplication(first_pos, second_pos):
    for k in random_list:
        print(f'значение из списка {k} имеет позицию {random_list.index(k)}')
    first_pos = int(input('Введите позицию первого числа: '))
    second_pos = int(input('Введите позицию первого числа: '))
    result = random_list[first_pos]*random_list[second_pos]
    return f'Результат умножения {random_list[first_pos]} на {random_list[second_pos]} будет равен = {result}'

print(multiplication(2, 3))

