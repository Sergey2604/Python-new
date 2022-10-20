# Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной последовательности.

lst = [454, 655, 64, 5441, 5641561, 561, 561, 561561, 561, 561, 56156]


def new_list(lst: list):
    new_lst = []
    for i in range(len(lst)):
        if new_lst.__contains__(lst[i]):
            continue
        else:
            new_lst.append(lst[i])
    print(new_lst)
    return new_lst


new_list(lst)
print(lst)
