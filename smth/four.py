maxa = 0
a = [61,228,9]
b = [i for i in range(len(a))]
for i in range(len(a)):
    n = a[i]
    while n // 10 > 0:
        n = n // 10
    b[i] = [n, a[i]]
b.sort(reverse=True)
s = ''
for i in range(len(b)):
    s += (str)(b[i][1])
print(s)