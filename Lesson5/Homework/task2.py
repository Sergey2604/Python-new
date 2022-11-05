# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

konfet = 2021


def first_player():
    global konfet
    num = int(input('Игрок 1, сколько конфет вы хотите взять? '))
    if num > 28 or num > konfet:
        print('Вы взяли конфет больше, чем можете унести с собой!')
    else:
        print(f'Игрок 1 взял {num} конфет, осталось {konfet - num}')
        if konfet - num == 0:
            print('Все конфеты достались игроку 1')
            exit()
        konfet -= num
    return konfet


def second_player():
    global konfet
    num = int(input('Игрок 2, сколько конфет вы хотите взять? '))
    if num > 28 or num > konfet:
        print('Вы взяли конфет больше, чем можете унести с собой!')
    else:
        print(f'Игрок 2 взял {num} конфет, осталось {konfet - num}')
        if konfet - num == 0:
            print('Все конфеты достались игроку 2')
            exit()
        konfet -= num
    return konfet


def game():
    global konfet
    lucky = random.randint(1, 3)
    if lucky == 1:
        print('Первый ход у игрока №1')
        while konfet > 0:
            first_player()
            second_player()
    else:
        print('Первый ход у игрока №2')
        while konfet > 0:
            second_player()
            first_player()


game()
