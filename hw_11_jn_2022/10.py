k = 0
for i in range(10**7 - 1, 0, -1):
    s = str(i)
    if s[0] == '9' and s[-1] == '7' and s.count('55') != 0 and s[1] != '5':
        k += 1
        w = int(s)
        sd = []
        for j in range(2, (int)(w**0.5)+1):
            if (w % j == 0) and (j**2 != w):
                sd.append(j)
                sd.append(w//j)
            if j**2 == w:
                sd.append(j)
        print(s, (sum(sd) + 1 + w) % 21)
    if k == 5:
        break