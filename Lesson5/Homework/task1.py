# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

lst = ['абв', 'hghj', 'jhgg', 'ghxdybjkuyughj', 'абвололлол', 'ромоироабв', 'рмпророммпрабвлдтдлывтдлтд', 'hjghxfxckj']


# def deleted(lst: list):
#     for i in lst:
#         if i.__contains__('абв'):
#             lst.remove(i)
#     print(lst)
#     return lst
#
#
# deleted(lst)
def deleted(lst: list):
    for i in lst:
        for j in range(len(i)):
            if i[j] == 'а' and i[j + 1] == 'б' and i[j + 2] == 'в':
                lst.remove(i)
    for i in lst: #Второй цикл для того, чтобы убрать все значения, которые пропустил первый цикл из-за смещения i
        for j in range(len(i)):
            if i[j] == 'а' and i[j + 1] == 'б' and i[j + 2] == 'в':
                lst.remove(i)
    print(lst)


deleted(lst)
