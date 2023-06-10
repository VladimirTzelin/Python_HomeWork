# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и
# не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint
list = int(input("Введите длину списка: "))
n_min = int(input("Введите значение мимнимума: "))
n_max = int(input("Введите значение максимума: "))
random_list = []

for i in range(0, list):
    random_list.append(randint(-5, 10))
    if n_max >= int(random_list[i]) >= n_min:
        print(f" x[{i}] = {random_list[i]},", end="")
print("\n", *random_list)

