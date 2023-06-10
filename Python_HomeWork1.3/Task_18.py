# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

import random
N = int(input("Введите число элементов массива: "))
num1 = num2 = 0
lis = []
lis_2 = []
for i in range(N-1):
    lis.append(random.randint(0, 20))
x = int(input("Введите искомое число: "))
lis.append(x)
lis_2 = sorted(lis)
lis_3 = sorted(lis_2, reverse=True)
print(lis)
i = 0
while i < N:
    if x > lis_2[i]:
        num1 = lis_2[i]
    if x < lis_3[i]:
        num2 = lis_3[i]
    i = i+1
d_1 = abs(num1 - x)
d_2 = abs(num2 - x)
print(f"Ближайшими к {x} являются значения {num1} и {num2}")
if d_1 > d_2:
    print(f"Из них ближе {num2}")
elif (d_1) < (d_2):
    print(f"Из них ближе {num1}")
else:
    print("?")
