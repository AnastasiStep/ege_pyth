i = int(input())
rez = ""

while (i > 0):
    rez = str(i % 2) + rez
    i = i // 2

print(rez)