f = open('27/3B.txt')
n = int(f.readline())
s = f.readlines()
ind = 0
maxa = 0
for i in range(0, len(s)):
    s[i]=int(s[i])
for i in range(0, n):
    if s[i] > maxa:
        maxa = s[i]
        ind = i
m = s[ind]
del(s[ind])
if m % 14 == 0:
    print(max(s) * m)
elif m % 7 == 0:
    maxa = 0
    for i in range(0, n - 1):
        if s[i] > maxa and (s[i] % 2 == 0):
            maxa = s[i]
    print(m * maxa)
elif m % 2 == 0:
    maxa = 0
    for i in range(0, n - 1):
        if s[i] > maxa and (s[i] % 7 == 0):
            maxa = s[i]
    print(m * maxa)
else:
    maxa = 0
    for i in range(0, n - 1):
        if s[i] > maxa and (s[i] % 14 == 0):
            maxa = s[i]
    print(m * maxa)