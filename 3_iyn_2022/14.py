n = (6*(343**1156)) - (5*(49**1147)) + (4*(7**1153)) - 875
print(n)
i = n
rez = ''
while (i > 0):
    rez = str(i % 7) + rez
    i = i // 7
print(rez)
i = (int)(rez)
summ = 0
while (i > 0):
    summ += i % 10
    i = i // 10
print(summ)