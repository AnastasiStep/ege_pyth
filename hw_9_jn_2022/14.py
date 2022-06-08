f = open('hw_9_jn_2022/14.txt')
l = (int)(f.readline())
maxa = 0
a = [[], []]
for j in range(l):
    n = f.readline().split(' ')
    a[0].append((int)(n[0]))
    a[1].append((int)(n[1]))
for i in range(l - 1):
    k = 0
    while (a[1][i] > a[0][i + 1]) and (i < l):
        i += 1
        k += 1
    if k > maxa:
        maxa = k
print(maxa + 1)
