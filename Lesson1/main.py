# 1.Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#
# *Примеры: *
#
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8, 9 -> нет
#
# 2.Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#
# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))

if a == b * b:
    print(f'число  {a} является квадратом {b}')
elif b == a * a:
    print(f'число  {b} является квадратом {a}')
else:
    print(f'число  {a} не является квадратом {b} и {b} не является квадратом {a}')


