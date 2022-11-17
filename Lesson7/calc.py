from datetime import datetime

import complex


def calc(a, b):
    if complex.operation == '+':
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'Число1: {a} {complex.operation} Число2: {b} Результат: {a + b}  Время: {datetime.now()}'+'\n')
        return a + b
    elif complex.operation == '-':
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'Число1: {a} {complex.operation} Число2: {b} Результат: {a - b}  Время: {datetime.now()}'+'\n')
        return a - b
    elif complex.operation == '*':
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'Число1: {a} {complex.operation} Число2: {b} Результат: {a * b}  Время: {datetime.now()}'+'\n')
        return a * b
    elif complex.operation == '/':
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(f'Число1: {a} {complex.operation} Число2: {b} Результат: {a / b}  Время: {datetime.now()}'+'\n')
        return a / b
