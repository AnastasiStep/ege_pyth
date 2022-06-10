f = open('hw_11_jn_2022/12.txt')
n = f.readline().split(' ')
l = int(n[0])
nach = int(n[1])
maxa = 0
k = []
for i in range(l):
    s = f.readline().split(' ')
    k.append([int(s[0]), 1])
    k.append([int(s[1]), -1])
k.sort()
o = []
u = 0
for i in range(len(k)):
    u += k[i][1]
    o.append(u)
print(max(o))
f = nach
for i in range(1, len(k)):
    d = k[i][0] - k[i-1][0]
    if o[i-1] != 0:
        f += d
print(f)