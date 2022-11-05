# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def from_file():
    file = ''
    with open('task4.txt', 'r', encoding='utf-8') as f:
        file = f.read()
    return file


def coding_to_file(file: str):
    print(f'Входные данные - {file}')
    count = 0
    previous = file[0]
    result = ''
    for i in range(len(file)):
        if file[i] == previous:
            count += 1
            if i == len(file) - 1:
                result += f'{count}{file[i]}'
        else:
            result += f'{count}{file[i - 1]}'
            count = 1
            previous = file[i]
    print(f'результат сжатия - {result}')
    return result


def to_file(result: str):
    with open('task4-result.txt', 'w', encoding='utf-8') as f:
        f.write(result)
    return


def result_from_file():
    result = ''
    with open('task4-result.txt', 'r', encoding='utf-8') as f:
        result = f.read()
    return result


def decoding(result: str):
    res = ''
    count = ''
    for i in result:
        if i.isdigit():
            count += i
        else:
            res += f'{i * int(count)}'
            count = ''
    print(f'результат декодирования - {res}')
    return res


def to_file_decoding(res: str):
    with open('task4-result-decoding.txt', 'w', encoding='utf-8') as f:
        f.write(res)


to_file(coding_to_file(from_file()))
to_file_decoding(decoding(result_from_file()))
