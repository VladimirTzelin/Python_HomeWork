# Задача 26:**
# Посчитать факториал (произведение 1 до N)  и треугольное число (сумма чисел от 1 до N)
# для числа N  **ЧЕРЕЗ РЕКУРСИЮ**

# def factorial(value):
#     if value == 1:
#         return value
#     else:
#         return value * factorial(value - 1)


# num_f = int(input("Введите число: \t"))
# print(f"Факториал \t{num_f} = {factorial(num_f)}")

# Cумма N чисел
# int(n*(n+1)//2)
#     n = 0  1  2  3  4   5   6   7   8   9   10  11  12  13  14   15   16   17   18   19   20
# tr(n) = 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210

def triangular_number(n):
    if n == 1:
        return 1
    return triangular_number(n-1) + n 


num_t = int(input("Введите число: "))
print(f"Треугольное число для {num_t} ->  {triangular_number(num_t)}")
