f = open('11_01_2022/26.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))

k = 0
srar = 0
maxi = 0

for i in range(len(a)-1):
    for j in range(len(a)):
        if j != i:
            if (a[i] % 2 == 0) and (a[j] % 2 == 0):
                srar = (a[i] + a[j])/2
                if srar in a:
                    k+=1
                    if (srar > maxi):
                        maxi = srar
print(k, maxi)