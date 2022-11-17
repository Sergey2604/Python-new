import csv


def writer():
    surname = input('Введите Фамилию: ')
    nam = input('Введите Имя: ')
    phone = input('Введите телефон: ')
    description = input('Введите описание: ')
    data = [[surname, nam, phone, description]]
    with open('base.csv', 'a', encoding='utf-8') as f:
        writ = csv.writer(f)
        for row in data:
            writ.writerow(row)



