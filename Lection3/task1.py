num = [1, 2, 3, 4, 5, 67, 8, 9]

lst = [(i, i ** 2) for i in num if i % 2 == 0]
print(lst)
