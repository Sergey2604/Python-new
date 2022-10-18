# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# # стоящих на нечётной позиции.
# #
# # Пример:
# #
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# lst = [5, 16, 98, 7, 1, 5, 6, 7, 9, 2, 16, 45]
# new_lst = []
# sum = 0
# for i in range(len(lst)):
#     if i % 2 != 0:
#         new_lst.append(lst[i])
#         sum += lst[i]
# print(f'Список из нечетных элементов: {new_lst}')
# print(f'Сумма нечетных элементов первоначального списка: {sum}')
#
# # Напишите программу, которая найдёт произведение пар чисел списка.
# # Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# #
# # Пример:
# #
# # - [2, 3, 4, 5, 6] => [12, 15, 16];
# # - [2, 3, 5, 6] => [12, 15]
#
# lst = [2, 3, 4, 5, 6]
#
#
# def multi(lst: list):
#     mult = 1
#     lst_multi = []
#     if len(lst) % 2 != 0:
#         for i in range(len(lst) // 2 + 1):
#             mult = lst[i] * lst[len(lst) - i - 1]
#             lst_multi.append(mult)
#     else:
#         for i in range(len(lst) // 2):
#             mult = lst[i] * lst[len(lst) - i - 1]
#             lst_multi.append(mult)
#
#     print(lst_multi)
#
#
# multi(lst)
#
# # Задайте список из вещественных чисел.
# # Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# #
# # Пример:
# #
# # - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
#
#
# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# minimum = 1
# maximum = 0
# for i in my_list:
#     if i - int(i) <= minimum:
#         minimum = i - int(i)
#     if i - int(i) >= maximum:
#         maximum = i - int(i)
# print(maximum-minimum)
#
# # Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# #
# # Пример:
# #
# # - 45 -> 101101
# # - 3 -> 11
# # - 2 -> 10
# num = int(input('Введите число: '))
# system_num = int(input('В какую систему перевести число: '))
#
#
# def numeric(num: int):
#     new_num = []
#     while num != 0:
#         new_num.append(round(num % system_num))
#         num //= system_num
#     new_num.reverse()
#     print('Мои вычисления - ', end=' ')
#     print(*new_num)
#     return new_num
#
#
# numeric(num)
# new_num = bin(num)
# print(f'Встроенная функция - {new_num}')
