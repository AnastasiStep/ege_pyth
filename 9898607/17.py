f = open('9898607/17.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))

k = 0
maxi = 0

for i in range(0, len(a)-1):
    for j in range(i + 1, len(a)):
        summ = a[i] + a[j]
        if (summ % 126 == 0):
            k+=1
            if (summ > maxi):
                maxi = summ

print(k, maxi)