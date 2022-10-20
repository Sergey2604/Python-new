# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import random

n = int(input())


def func(n):
    i = 2
    lst = []
    old_n = n
    while i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old_n} приведены в списке: {lst}")
    return lst


func(n)
