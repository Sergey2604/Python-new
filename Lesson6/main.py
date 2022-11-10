import binascii

n = '5+6*10/30'

num = ''

for i in range(len(n)):
    if n[i].isdigit():
        num += n[i]
    else:
        num += ''
print(num)