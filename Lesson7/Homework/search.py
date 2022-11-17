import csv


def searc():
    sear = input('Введите искомую фамилию: ')
    with open('base.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row.__contains__(f'{sear}'):
                print(*row)



