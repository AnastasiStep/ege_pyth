fin = open('09_02_2022/26.txt')
m = 10000
n = int(fin.readline())
a = []
for i in range(m+1):
    a.append([0] * (m+1))
for i in range(n):
    s = fin.readline()
    x, y = map(int, s.split())
    a[x][y] = 1
ma, mai = 0, 0
for i in range(m):
    f = 66
    k = 0
    for j in range(m):
        if a[i][j] == 1 and f == 66:
            f = 77
            k = k + 1
        elif a[i][j] == 1 and f == 77:
            k = k + 1
        elif a[i][j] == 0 and f == 77:
            if k > ma:
                ma = k
                mai = i
            k = 0
            f == 66
print(ma, mai)
