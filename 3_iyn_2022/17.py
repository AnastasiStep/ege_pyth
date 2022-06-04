f = open('3_iyn_2022/17.txt')
s = [i for i in f]
for i in range(len(s)):
    s[i] = (int)(s[i])
print(s)
kk = 0
summ = 0
for i in range(len(s) - 2):
    k = 0
    for j in range(0,3):
        n = s[i + j]
        b = ''
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        c0 = b.count('0')
        c1 = b.count('1')
        if c0 >= 1 and c1 == 2:
            k += 1
    if k > 1:
        kk += 1
        summ += max(s[i], s[i + 1], s[i + 2])
print(kk, summ)