# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. Приоритет операций стандартный

def app(txt):
    if '(' in txt:
        start = 0
        for i in range(len(txt)):
            if txt[i] == '(':
                start = i
        fin = start + txt[start:].index(')')
        tmp = txt[start+1:fin]
        result = app(tmp)
        return app(f'{txt[:start]}{result}{txt[fin+1:]}')
    sign = ''
    for s in '+-*/':
        if s in txt:
            sign = s
            break
    if sign == '':
        return int(txt)
    else:
        a, b = txt.split(sign)
        if sign == '*': return app(a)*app(b)
        elif sign == '/': return app(a)/app(b)
        elif sign == '+': return app(a)+app(b)
        elif sign == '-': return app(a)-app(b)


print(app('(7+3)*(11-3)/2'))
