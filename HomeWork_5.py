# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# A = int(input("Укажите число: "))
# B = int(input("Укажите степень числа: "))
# def power(A, B):
#     if (B == 1):
#         return (A)
#     if (B != 1):
#         return (A * power(A, B - 1))

# print(f"Итоговый результат: {A}**{B} = {power(A, B)}")


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число число: "))
# def summa(a, b):
#     a += 1
#     b -= 1
#     if b > 0:
#         return summa(a, b)
#     else:
#         return a
 
# print (summa(a, b))