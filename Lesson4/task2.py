# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
#
# 2) с помощью дополнительных библиотек Python

# from cmath import sqrt


# def find_solution(a, b, c):
#     d = b * b - 4 * a * c
#     if d < 0:
#         print('No solutions')
#     elif d == 0:
#         print(-b / (2 * a))
#     else:
#         list_ = []
#         list_.append((-b - d**0.5) / (2 * a))
#         list_.append((-b + d**0.5) / (2 * a))
#         print(list_)


# print('Input A, B, C for Ax^2 + Bx + C')
# a = int(input("A: "))
# b = int(input("B: "))
# c = int(input("C: "))

# find_solution(a, b, c)
import sympy
import sympy as sm
a = int(input())
b = int(input())
c = int(input())
x = sm.Symbol('x')
print(sm.solveset(a * x ** 2 + b * x + c, x))

