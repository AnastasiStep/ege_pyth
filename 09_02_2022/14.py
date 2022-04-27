i = 3*343**8 + 5*49**12 + 7**15 - 49
rez = ''

while (i > 0):
    rez = str(i % 7) + rez
    i = i // 7

print(rez)