# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def bin_update(number):
    return bin(number)[2:]

# Искомый вывод
print(bin(45))
print(bin(3))
print(bin(2))

# Использование преобразователя
print(bin_update(45))
print(bin_update(3))
print(bin_update(2))