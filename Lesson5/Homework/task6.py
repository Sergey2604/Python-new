# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('task6-1.txt', 'w', encoding='utf-8') as file:
    file.write('2*x^2 + 5*x^5')
with open('task6-2.txt', 'w', encoding='utf-8') as file:
    file.write('23*x^4 + 9*x^6')

with open('task6-1.txt','r') as file:
    file1 = file.readline()
    file1_lst = file1.split()


with open('task6-2.txt','r') as file:
    file2 = file.readline()
    file2_lst = file2.split()

print(f'{file1_lst} + {file2_lst}')
sum_poly = file1_lst + file2_lst

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f'{file1_lst} + {file2_lst}')