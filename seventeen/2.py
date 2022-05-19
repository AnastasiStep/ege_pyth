f = open('seventeen/2.txt')
s = [i for i in f]
for p in range(0, len(s)):
    s[p] = (int)(s[p])
k = 0
summ = 0
for i in range(0, len(s) - 1):
    for j in range(0, len(s) - 1):
        if ((s[i] - s[j]) % 2 == 0) and ((s[i] % 19 == 0) or (s[j] % 19 == 0)):
            k+=1
            print(k)
            if (s[i] + s[j] > summ):
                summ = s[i] + s[j]
print(k, summ)