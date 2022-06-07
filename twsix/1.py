f = open('twsix/1.txt')
t = f.readline().split(' ')
n = (int)(t[0])
su = (int)(t[1])
A = []
B = []
for i in range(n):
    s = f.readline()
    s = s.split(' ')
    if s[1] == 'A\n':
        A.append((int)(s[0]))
    else:
        B.append((int)(s[0]))
A = sorted(A)
B = sorted(B)
C = sorted(A + B)

summ = 0
k = 0
for i in C:
    if (summ + i) < su:
        k += 1
        summ = summ + i


summb = 0
kb = 0
for i in B:
    if summb + i < su:
        kb += 1
        summb = summb + i

ka = k - kb
summa = 0
for i in range(len(A)):
        if i < ka:
            summa = summa + A[i]

summm = summa + summb
while summm >= su:
    summb -= B[kb]
    kb -= 1
    ka += 1
    summa += A[ka]
    summm = summa + summb
summb = 0
for i in range(len(B)):
        if i < kb:
            summb = summb + B[i]
summa = 0
for i in range(len(A)):
        if i < ka:
            summa = summa + A[i]
summm = summb + summa
print(kb, su - summm)