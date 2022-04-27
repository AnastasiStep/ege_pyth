f = open('var3/26.txt')
a = []
n = int(f.readline())
s = 0
maxc = 0
for i in f:
    x = int(i)
    if x <= 22:
        s += x
    else:
        a.append(x)
a.sort()
for i in range(len(a)):
    if i < len(a)//2:
        s += a[i]*0.85
        maxc = a[i]
    else:
        s += a[i]
print(s, maxc)