i = 50
rez = ""

while (i > 0):
    rez = str(i % 4) + rez
    i = i // 4

print(rez)