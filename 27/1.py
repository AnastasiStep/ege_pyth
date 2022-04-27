f = open('27/1B.txt')
n = int(f.readline())
mina = 100000000
summa = 0
for i in range(n):
    s = f.readline().split()
    a1 = max(int(s[0]), int(s[1]))
    a2 = min(int(s[0]), int(s[1]))
    summa += a1
    if (a1 - a2) < mina and (a1 - a2) % 3 != 0:
        mina = a1 - a2
if summa % 3 == 0:
    summa -= mina
print(summa)