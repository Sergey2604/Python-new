# # Вычислить число c заданной точностью d
# #
# # Пример:
# #
# # - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# num = float(input('Введите число: '))
# d = float(input('Введите, с какой точностью произвести вычисления: '))
#
#
# def func(num: float, d: float):
#     count = 0
#     while d != 1:
#         count += 1
#         d *= 10
#     return round(num, count)
#
#
# print(func(num, d))
#
# # Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# import random
#
# n = int(input())
#
#
# def func(n):
#     i = 2
#     lst = []
#     old_n = n
#     while i <= n:
#         if n % i == 0:
#             lst.append(i)
#             n //= i
#             i = 2
#         else:
#             i += 1
#     print(f"Простые множители числа {old_n} приведены в списке: {lst}")
#     return lst
#
#
# func(n)
#
# # Задайте последовательность чисел. Напишите программу, которая
# # выведет список неповторяющихся элементов исходной последовательности.
#
# lst = [454, 655, 64, 5441, 5641561, 561, 561, 561561, 561, 561, 56156]
#
#
# def new_list(lst: list):
#     new_lst = []
#     for i in range(len(lst)):
#         if new_lst.__contains__(lst[i]):
#             continue
#         else:
#             new_lst.append(lst[i])
#     print(new_lst)
#     return new_lst
#
#
# new_list(lst)
# print(lst)
#
# # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# #
# # Пример:
# #
# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#
# num = int(input())
# lst = [0] * (num * 2 + 1)
# lst[num + 1] = 1
# for i in range(num + 2, num * 2 + 1):
#     lst[i] = lst[i - 1] + lst[i - 2]
# for i in range(num, -1, -1):
#     lst[i] = lst[i + 2] - lst[i + 1]
# print(lst)
