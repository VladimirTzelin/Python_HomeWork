# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод #  — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за
# один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
i= 0
n_bushes = list(randint(0, 6)
                for i in range(int(input("Укажите кол-во кустов: "))))
bush_number = int(input("Укажите номер куста: "))
print(f"Урожайность кустов {n_bushes}")

if bush_number == 1:
    harvest = n_bushes[0] + n_bushes[1] + n_bushes[-1]
elif bush_number == len(n_bushes):
    harvest = n_bushes[-2] + n_bushes[-1] + n_bushes[0]
else:
    harvest = n_bushes[bush_number-1] + \
        n_bushes[bush_number-2] + n_bushes[bush_number]
print(f"Урожай {harvest} ягод")
