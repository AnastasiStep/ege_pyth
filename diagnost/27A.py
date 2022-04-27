f = open('diagnost/27A.txt')
n = int(f.readline())
a = [int(s) for s in f]

k = 30
smax = -300000000
for i in range(n):
    s = 0
    t = 0
    for j in range(i, n):
        s += a[j]
        t += (a[j]>0 and a[j]%2 == 0)
        if t % k == 0 and s > smax:
            smax = s
print(smax)