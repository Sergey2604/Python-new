# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input())


def koefficients(k: int):
    return f'{random.randint(0, 101)}*(x**{k}) + {random.randint(0, 101)}*x + {random.randint(0, 101)} = 0'


def to_file():
    with open('task5.txt', 'w', encoding='utf-8') as f:
        f.write(koefficients(k))


koefficients(k)
to_file()
