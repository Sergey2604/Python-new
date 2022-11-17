# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему
# логирования.




print('1 - Комплексные числа')
print('2 - Рациональные числа')
print('3 - Посмотреть логи')
menu = input('Выберите, какое действие надо произвести: ')
if menu == '1':
    from calc import calc
    print(calc(complex(input('Введите комплексное число 1: ')), complex(input('Введите комплексное число 2: '))))
elif menu == '2':
    from calc import calc
    print(calc(float(input('Введите комплексное число 1: ')), float(input('Введите комплексное число 2: '))))
elif menu=='3':
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.read()
