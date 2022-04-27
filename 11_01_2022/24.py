f = open('11_01_2022/24.txt')
s = f.readlines()
a = []
for i in s:
    a.append(i)

k = 0
mina = len(str(a[0]))
s = 0

for i in range(len(a)):
    k = str(a[i]).count('G')
    if (k < mina):
        mina = k
        s = i
print(s, mina)
