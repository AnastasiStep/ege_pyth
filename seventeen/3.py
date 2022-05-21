f = open('seventeen/3.txt')
s = [i for i in f]
for i in range(len(s)):
    s[i] = (int)(s[i])
k = 0
summ = 0
for i in range(0, len(s) - 1):
    srar = (s[i] + s[i + 1])/2
    if ((s[i] % 3 == 0) or (s[i + 1] % 3 == 0)) and ((s[i] < srar) or (s[i + 1] < srar)):
        k+=1
        summ = max(summ, s[i] + s[i + 1])
print(k, summ)
#3101 19730