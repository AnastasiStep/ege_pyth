f = open('seventeen/4.txt')
s = [i for i in f]
for i in range(len(s)):
    s[i] = (int)(s[i])
k = 0
summ = 0
mina = max(s)
for i in range(len(s)):
    if s[i] % 21 == 0:
        mina = min(mina, s[i])
for i in range(len(s) - 1):
    if (s[i] % mina == 0) or (s[i + 1] % mina == 0):
        k += 1
        summ = max(summ, s[i] + s[i + 1])
print(k, summ)
#126 171120