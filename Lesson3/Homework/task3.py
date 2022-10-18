# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_list = [1.1, 1.2, 3.1, 5, 10.01]
minimum = 1
maximum = 0
for i in my_list:
    if i - int(i) <= minimum:
        minimum = i - int(i)
    if i - int(i) >= maximum:
        maximum = i - int(i)
print(maximum-minimum)