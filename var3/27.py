f = open('var3/27.txt')
n = int(f.readline())
a = [0] * 158
l = 0
r = 0
for i in range(n):
    x = int(f.readline())
    p = x % 158
    if a[(158 - p) % 158] > x and a[(158 - p) % 158] + x > l + r:
        l = a[(158 - p) % 158]
        r = x
    if x > a[p]: a[p] = x
print(l, r)