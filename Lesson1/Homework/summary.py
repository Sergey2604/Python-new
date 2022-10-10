# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
#
# def Weekend(day):
#     if day == 6 or day == 7:
#         print('да')
#     elif 0<day<6:
#         print('нет')
#     else:
#         print('Введите верное значение дня недели')
#
#
# day = int(input('Введите число дня недели: '))
# Weekend(day)
#
#
# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#
# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             print(x, 'OR', y, 'OR', z, '=', x and y and z)
#
#
#
# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
#
# def Coords(x, y):
#     if x > 0 and y > 0:
#         print('1')
#     elif x < 0 and y > 0:
#         print('2')
#     elif x < 0 and y < 0:
#         print('3')
#     elif x > 0 and y < 0:
#         print('4')
#
#
# x = float(input('Введите координаты оси X: '))
# y = float(input('Введите координаты оси Y: '))
# Coords(x, y)
#
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)
#
# def coords(number):
#     if number==1:
#         print('x>0 and y>0')
#     elif number==2:
#         print('x<0 and y>0')
#     elif number==3:
#         print('x<0 and y<0')
#     elif number==4:
#         print('x>0 and y<0')
#     else:
#         print('Введите верный номер четверти')
#
# number=int(input('Введите номер четверти: '))
# coords(number)
#
#
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# import math
#
#
# def distance(x1, y1, x2, y2):
#     dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     print(f'расстояние между двумя заданными точками - {dist}')
#
#
# x1 = float(input('Введите координаты оси Х для точки А: '))
# y1 = float(input('Введите координаты оси Y для точки А: '))
# x2 = float(input('Введите координаты оси Х для точки B: '))
# y2 = float(input('Введите координаты оси Y для точки B: '))
# distance(x1, y1, x2, y2)
