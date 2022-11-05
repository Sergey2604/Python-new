# Создайте программу для игры в ""Крестики-нолики"".
import random

# size = int(input('Введите размер поля: '))


def krest_zero():
    num1 = num2 = num3 = num4 = num5 = num6 = num7 = num8 = num9 = ''
    pol = f'{num7} | {num8} | {num9} |\n' \
          f'{num4} | {num5} | {num6} |\n' \
          f'{num1} | {num2} | {num3} |'
    first_turn = random.randint(1, 3)
    while num1 =='' or num2 =='' or num3 =='' or num4 =='' or num5 =='' or num6 =='' or num7 =='' or num8 =='' or num9 == '':
        match first_player():
            case 1:
                num1 = 'X'
            case 2:
                num2 = 'X'
            case 3:
                num3 = 'X'
            case 4:
                num4 = 'X'
            case 5:
                num5 = 'X'
            case 6:
                num6 = 'X'
            case 7:
                num7 = 'X'
            case 8:
                num8 = 'X'
            case 9:
                num9 = 'X'
        print(pol)
        second_player()
        match second_player:
            case 1:
                num1 = 'O'
            case 2:
                num2 = 'O'
            case 3:
                num3 = 'O'
            case 4:
                num4 = 'O'
            case 5:
                num5 = 'O'
            case 6:
                num6 = 'O'
            case 7:
                num7 = 'O'
            case 8:
                num8 = 'O'
            case 9:
                num9 = 'O'
        print(pol)

    if num1 == num2 == num3 == 'X' or num4 == num5 == num6 == 'X' or num7 == num8 == num9 == 'X' or num1 == num4 == num7 == 'X' \
            or num2 == num5 == num8 == 'X' or num3 == num6 == num9 == 'X' or num1 == num5 == num9 == 'X' or num3 == num5 == num7 == 'X':
        print('Выиграл игрок 1!')
        exit()
    elif num1 == num2 == num3 == 'O' or num4 == num5 == num6 == 'O' or num7 == num8 == num9 == 'O' or num1 == num4 == num7 == 'O' \
            or num2 == num5 == num8 == 'O' or num3 == num6 == num9 == 'O' or num1 == num5 == num9 == 'O' or num3 == num5 == num7 == 'O':
        print('Выиграл игрок 1!')
        exit()


# def pole():


def first_player():
    turn = int(input('Игрок 1, выберите место, куда вы хотите сходить. Расположение клеток: 7 | 8 | 9 |\n'
                     '                                                                      4 | 5 | 6 |\n'
                     '                                                                      1 | 2 | 3 |\n'))
    return turn


def second_player():
    turn = int(input('Игрок 2, выберите место, куда вы хотите сходить. Расположение клеток: 7 | 8 | 9 |\n'
                     '                                                                      4 | 5 | 6 |\n'
                     '                                                                      1 | 2 | 3 |\n'))
    return turn


krest_zero()
