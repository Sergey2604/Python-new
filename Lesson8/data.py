import csv


def number_id():
    with open('base.csv', 'r', encoding='utf-8') as f:
        id = len(f.read().splitlines())
    return id


def fill_data():
    fio = input('Введите ФИО: ')
    phone = input('Введите телефон: ')
    post = input('Введите должность: ')
    department = input('Введите отдел работника: ')
    id = number_id()
    with open('base.csv', 'a+', encoding='utf-8') as f:
        f.write(f'{id}; {fio}; {phone}; {post}; {department}\n')


def reader():
    with open('base.csv', 'r', encoding='utf-8') as f:
        reade = csv.reader(f)
        for row in reade:
            print(*row)
