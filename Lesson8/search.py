import csv


def searc():
    sear = input('Введите искомые данные: ')
    with open('base.csv', 'r', encoding='utf-8') as f:
        for row in f.readlines():
            if sear in row:
                print(row)