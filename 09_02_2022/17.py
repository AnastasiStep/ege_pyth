f = open('09_02_2022/17.txt')
a = [int(s) for s in f]
count2 = s2 = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        count2 += 1
        s2 += a[i]
sr = s2 / count2
count1 = 0
m = 0
for i in range(len(a) - 1):
    if (a[i] % 5 == 0 and a[i + 1] % 5 != 0 and a[i + 1] < sr) or (a[i] % 5 != 0 and a [i + 1] % 5 == 0 and a[i] < sr):
        count1 += 1
        m = max(m, a[i] + a[i + 1])
print(count1, m)
