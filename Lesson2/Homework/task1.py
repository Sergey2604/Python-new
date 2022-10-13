# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11


number = input('Введите вещественное или целое число: ')


def summary(num):
    summ = 0
    lst = []
    i = 0
    for j in number:
        if j == '.' or j == ',':
            j = 0
        lst.append(int(j))
        summ = summ + lst[i]
        i += +1
    print(f'Сумма цифр введенного числа = {summ}')
    return summ


summary(number)
