# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = [2, 3, 4, 5, 6]


def multi(lst: list):
    mult = 1
    lst_multi = []
    if len(lst) % 2 != 0:
        for i in range(len(lst) // 2 + 1):
            mult = lst[i] * lst[len(lst) - i - 1]
            lst_multi.append(mult)
    else:
        for i in range(len(lst) // 2):
            mult = lst[i] * lst[len(lst) - i - 1]
            lst_multi.append(mult)

    print(lst_multi)


multi(lst)
