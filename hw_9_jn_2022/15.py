f = open('hw_9_jn_2022/15.txt')
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
p = []
for i in range(len(b[0])):
    k = 0
    for j in range(1, 9):
        if b[1][i].count((str)(j)) == 0:
            k += 1
    p.append(k)
print(max(p))
o = []
for i in range(len(b[0])):
    k = 0
    for j in range(1, 9):
        if b[1][i].count((str)(j)) == 0:
            k += 1
    if k == max(p):
        o.append(b[0][i])
print(max(o))