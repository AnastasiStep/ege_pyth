f = open('09_02_2022/27A.txt')
n = int(f.readline())
s = 0
res = []
maxs = [0] + [False]*998
lens = [0] + [False]*998
for i in range(1, n+1):
    s += int(f.readline())
    ost = s%999
    if maxs[ost] != False:
        res.append([s-maxs[ost], lens[ost]-i])
    else:
        maxs[ost] = s
        lens[ost] = i
print(len(res))