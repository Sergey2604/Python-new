# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# *Пример: *
# - Для
# N = 5: 1, -3, 9, -27, 81
#

#

# n = int(input())
# a = []
# for i in range(n):
#     a.append((-3) ** i)
# print(*a, sep=', ')



string_input = input('Введите текст: ')
string_elevent = input('Введите элемент для поиска: ')
print(string_input.count(string_elevent))

