with open('17.txt') as f:
    a = list(map(int, f.readlines))
kch = 0
sch = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        kch += 1
        sch += a[i]
sr = sch/kch
for i in range(len(a)):
    if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and 