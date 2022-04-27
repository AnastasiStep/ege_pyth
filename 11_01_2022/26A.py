f = open('11_01_2022/26A.txt')
n = int(f.readline())
e = []
for i in range(n):
    x = int(f.readline())
    e.append(x)

maxsumma = 0

for i1 in range(len(e)):
    for i2 in range(len(e)):
        if i1 != i2:
            for i3 in range(len(e)):
                if (i1 != i3) and (i2 != i3):
                    summa = e[i1] + e[i2] + e[i3]
                    if summa % 3 == 0:
                        if summa > maxsumma:
                            maxsumma = summa
                            print(maxsumma)
print(maxsumma)