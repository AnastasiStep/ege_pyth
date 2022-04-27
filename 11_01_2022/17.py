f = open('11_01_2022/17.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))

k = 0
maxi = 0

for i in range(1, len(a)-1):
    if ((a[i - 1] + a[i] > a[i + 1]) and (a[i] + a[i + 1] > a[i - 1]) and (a[i - 1] + a[i + 1] > a[i])):
        k += 1
        summa = a[i - 1] + a[i] + a[i + 1]
        if (summa > maxi):
            maxi = summa
print(k, maxi)