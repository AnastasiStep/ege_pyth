f = open('hw_9_jn_2022/16.txt')
n = (int)(f.readline())
a = []
for i in range(n):
    s = f.readline().split(' ')
    a.append([(int)(s[0]), (int)(s[1])])
a.sort(key=lambda x: x[1])
a.sort()
maxa = 0
maxi = 0
k = 0
for i in range(1, len(a)):
    if a[i][0] == a[i - 1][0]:
        if a[i][1] % 2 != 0:
            k+=1
    else:
        k = 0
        if a[i][1] % 2 != 0:
            k+=1
    if k > maxa:
        maxa = k
        maxi = a[i][0]
print(maxa, maxi)