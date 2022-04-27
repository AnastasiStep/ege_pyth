f = open('fr/17.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))

k = 0
maxi = 0

for i in range(0, len(a)-1):
    summ = a[i] + a[i+1]
    if (summ % 7 == 0 and (a[i] % 5 == 0 or a[i + 1] % 5 == 0)):
        k+=1
        if (summ > maxi):
            maxi = summ

print(k, maxi)