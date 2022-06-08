f = open('hw_9_jn_2022/16.txt')
n = (int)(f.readline())
a = [[],[]]
for i in range(n):
    s = f.readline().split(' ')
    a[0].append((int)(s[0]))
    a[1].append((int)(s[1]))
b = [[], []]
for i in range(len(a[0])):
    if b[0].count(a[0][i]) != 0:
        b[1][b[0].index(a[0][i])] += (str)(a[1][i])
    else:
        b[0].append(a[0][i])
        b[1].append((str)(a[1][i]))
p = [[], []]
for i in range(len(b[0])):
    k = 0
    for j in range(0, len(b[1][i]), 2):
        if (int)((b[1][i])[j]) % 2 != 0:
            k += 1
    p[0].append(b[0][i])
    p[1].append(k)
print(max(p[1]), p[0][p[1].index(max(p[1]))])