# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))


def multi(num):
    mul = 1
    lst1=[]
    lst2=[]
    for i in range(1, num + 1):
        mul *= i
        lst1.append(i)
        lst2.append(mul)
    print(lst1)
    print(lst2)


multi(num)
