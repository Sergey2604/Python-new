# 3.Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество
# вхождений одной строки в другой.

some_str_1 = input()
some_str_2 = input()
len_str_2 = len(some_str_2)
i = 0
count = 0
while i < len(some_str_1):
    if some_str_1[i:i + len_str_2] == some_str_2:
        count += 1
    i += 1
print(count)
