f = open('hw_9_jn_2022/14.txt')
l = (int)(f.readline())
maxa = 0
k = []
for i in range(l):
    s = f.readline().split(' ')
    a = (int)(s[0])
    b = (int)(s[1])
    k.append([a,1])
    k.append([b,-1])
k.sort()
o = []
u = 0
for i in range(len(k)):
    u += k[i][1]
    o.append(u)
print(max(o))
f = 0
for i in range(1, len(k)):
    d = k[i][0] - k[i-1][0]
    if o[i-1] != 0:
        f += d
print(f)