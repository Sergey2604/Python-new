# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# Пример:
#
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input('Введите число: '))


def primer(num):
    lst = []
    summ = 0
    for i in range(1, num + 1):
        lst.append(round((1 + (1 / i)) ** i, 2))
        summ += round((1 + (1 / i)) ** i, 2)
    print(lst)
    print(summ)


primer(num)