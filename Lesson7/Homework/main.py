from Lesson7.Homework import writer, reader, search

print('Какое действие Вы хотите совершить?')
print('1-запись в файл')
print('2-чтение из файла')
print('3 - поиск данных')
choice = input()
if choice == '1':
    writer.writer()
elif choice == '2':
    reader.reade()
elif choice == '3':
    search.searc()
