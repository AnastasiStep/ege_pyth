f = open('3_iyn_2022/27B.txt')
n = (int)(f.readline())
summ = 0
while True:
    s = f.readline()
    if s == '':
        break
    a = s.split(' ')
    for i in range(len(a)):
        a[i] = (int)(a[i])
    n = a[0]
    b = [i for i in range(len(a) - 1)]
    for i in range(1, len(a)):
        b[i - 1] = a[i]
    b.sort()
    summa = sum(b)
    j = 0
    while (summa % 2 != 0) and (j < len(b) - 1):
        if j == 0:
            summa = summa - b[j]
        else:
            summa = summa + b[j] - b[j + 1]
        j += 1
    summ = summ + summa
    while (summ % 5 == 0) and (j < len(b) - 1):
        summa = b[j] - b[j + 1]
        summ = summ + summa
        j += 1
    print(n, b, summ)