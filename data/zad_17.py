f = open('data/dla_zad_17.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))

maxa = 0;
suma = 0

for i in range(len(a)-1):
    if ((a[i] % 13 == 4) and (a[i] % 8 == 1)):
        suma += a[i]
        if (a[i] > maxa):
            maxa = a[i]

print(maxa, suma)