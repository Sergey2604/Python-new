# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11
#
#
# number = input('Введите вещественное или целое число: ')
#
#
# def summary(num):
#     summ = 0
#     lst = []
#     i = 0
#     for j in number:
#         if j == '.' or j == ',':
#             j = 0
#         lst.append(int(j))
#         summ = summ + lst[i]
#         i += +1
#     print(f'Сумма цифр введенного числа = {summ}')
#     return summ
#
#
# summary(number)
#
# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# #
# # Пример:
# #
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#
# num = int(input('Введите число: '))
#
#
# def multi(num):
#     mul = 1
#     lst1=[]
#     lst2=[]
#     for i in range(1, num + 1):
#         mul *= i
#         lst1.append(i)
#         lst2.append(mul)
#     print(lst1)
#     print(lst2)
#
#
# multi(num)
#
# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# #
# # Пример:
# #
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# num = int(input('Введите число: '))
#
#
# def primer(num):
#     lst = []
#     summ = 0
#     for i in range(1, num + 1):
#         lst.append(round((1 + (1 / i)) ** i, 2))
#         summ += round((1 + (1 / i)) ** i, 2)
#     print(lst)
#     print(summ)
#
#
# primer(num)
