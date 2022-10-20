# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
num = float(input('Введите число: '))
d = float(input('Введите, с какой точностью произвести вычисления: '))


def func(num: float, d: float):
    count = 0
    while d != 1:
        count += 1
        d *= 10
    return round(num, count)


print(func(num, d))
