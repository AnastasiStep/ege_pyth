f = open('seventeen/1.txt')
s = [i for i in f]
for p in range(0, len(s)):
    s[p] = (int)(s[p])
k = 0
summ = 0
for p in range(0, len(s) - 1):
    if (s[p] % 3 == 0) or (s[p + 1] % 3 == 0):
        k += 1
        if s[p] + s[p + 1] > summ:
            summ = s[p] + s[p + 1]
print(k, summ)