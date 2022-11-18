import search,data


def menu():
    print('Какое действие Вы хотите совершить?')
    print('1-запись в файл')
    print('2-чтение из файла')
    print('3 - поиск данных')
    choice = input()
    if choice == '1':
        data.fill_data()
    elif choice == '2':
        data.reader()
    elif choice == '3':
        search.searc()
