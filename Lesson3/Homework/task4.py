# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
num = int(input('Введите число: '))
system_num = int(input('В какую систему перевести число: '))


def numeric(num: int):
    new_num = []
    while num != 0:
        new_num.append(round(num % system_num))
        num //= system_num
    new_num.reverse()
    print('Мои вычисления - ', end=' ')
    print(*new_num)
    return new_num


numeric(num)
new_num = bin(num)
print(f'Встроенная функция - {new_num}')
