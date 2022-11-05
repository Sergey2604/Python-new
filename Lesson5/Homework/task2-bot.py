# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random

konfet = 2021


def player():
    global konfet
    num = int(input('Игрок, сколько конфет вы хотите взять? '))
    if num > 28 or num > konfet:
        print('Вы взяли конфет больше, чем можете унести с собой!')
    else:
        print(f'Игрок взял {num} конфет, осталось {konfet - num}')
        if konfet - num == 0:
            print('Все конфеты достались игроку')
            exit()
        konfet -= num

    return konfet


def bot():
    global konfet
    if konfet > 0:
        num = random.randint(1, 29)
        if num>konfet:
            num = random.randint(1, konfet)
        print(f'Бот взял {num} конфет, осталось {konfet - num}')
        if konfet - num == 0:
            print('Все конфеты достались боту')
            exit()
        konfet -= num
    return konfet


def game():
    global konfet
    lucky = random.randint(1, 3)
    if lucky == 1:
        print('Первый ход у игрока')
        while konfet > 0:
            player()
            bot()
    else:
        print('Первый ход у бота')
        while konfet > 0:
            bot()
            player()


game()
