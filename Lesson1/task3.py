# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от - N до N

# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не30.

# a = int(input())
# for i in range(-a, a + 1, 1):
#     print(i, end=",")

# n = float(input())
# if n % 1 == 0:
#     print('no')
# else:
#     print((int(n * 10) % 10))
# n = input()
# if '.' in n:
#     index_t = n.find('.')
#     print(n[index_t + 1])
# else:
#     print('нет')


num=int(input('Введите число '))
if ((num % 5 == 0 and not num % 30 == 0) and num % 10 == 0) or num % 15 == 0 and (not num % 30 == 0):
    print('da')
else:
    print('net')