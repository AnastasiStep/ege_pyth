f = open('11.txt')
a = []
n = int(f.readline())
s = 0
maxc = 0
for i in f:
    x = int(i)
    if x <= 200: #поменять!!!!!!!!!!!!
        s += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a)//2:
        s += a[i]*0.55 #поменять!!!!!!!!!!!!
        maxc = a[i]
    else:
        s += a[i]
print(s, maxc)