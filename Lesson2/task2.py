# 2. Для натурального n создать словарь индекс - значение, состоящий из элементов последовательности 3n + 1.
#
# *Пример: *
# - Для
# n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n=int(input('введите число:'))
# for i in range(1,n+1):
#     print(f'{i}: {3*i+1}')

n = int(input())
print('{', end='')
for i in range(1, n):
    print(f'{i}:{3 * i + 1}', end=', ')
print(f'{n}:{3 * n + 1}', end='}')