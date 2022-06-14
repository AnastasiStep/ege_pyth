f = open('hw15_jn_2022/18B.txt')
l = int(f.readline())
s = f.readlines()
for i in range(len(s)):
    s[i] = int(s[i])

sd = []
for i in range(len(s) - 1):
    summ  = 0
    for j in range(i, len(s)):
        f = 0
        for n in range(2, int(s[j]**0.5) + 1):
            if s[i] % n == 0:
                f = 1
                break
        if f == 0:
            summ += 1
        if summ % 9 == 0 and summ != 0:
            sd.append(summ)
print(max(sd))

#A - 90
#B - ??