# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
#
# Реализуйте алгоритм перемешивания списка.
from random import Random, shuffle

num = int(input('Введите число: '))


def fill_list(num):
    lst = []
    for i in range(-num, num + 1):
        lst.append(i)
    shuffle(lst)
    print(f'Список элементов от -{num} до {num} - {lst}')
    return lst


def fill_file(lst: list):
    length = len(lst)
    print(f'количество элементов - {length}')
    with open('file.txt', 'w') as f:
        f.write(f'{str(round(Random().randrange(0, length)))}\n')
        f.write(f'{str(round(Random().randrange(0, length)))}\n')
        f.write(f'{str(round(Random().randrange(0, length)))}\n')
        return lst


def read_file(lst: list):
    indexes = []
    with open('file.txt', 'r') as file:
        for i in file:
            indexes.append(int(i.strip()))
    print(f'индексы - {indexes}')
    return indexes


def multiply(lst: list, index: list):
    elem = []
    multi = 1
    for i in range(len(index)):
        elem.append(lst[index[i]])
    print(f'Найденные элементы по индексу - {elem}')
    for i in elem:
        multi *= i
    print(f'результат - {multi}')


multiply(fill_file(fill_list(num)), read_file(fill_list(num)))
