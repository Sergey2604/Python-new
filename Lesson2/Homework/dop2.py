# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

lst1 = [1, 2, 3, 2, 0]
lst2 = [5, 1, 2, 7, 3, 2]

result=[]
for i in lst1:
    if result.__contains__(i):
        continue
    for j in lst2:
        if j==i:
            result.append(j)
print(result)