s = '9__55_7'
for i1 in range(0,10):
    for i2 in range(0,10):
        for i3 in range(0,10):
            w = 9000000 + (i1 * 100000) + (i2 * 10000) + 5000 + 500 + (i3 * 10) + 7
            #print(w)

for i in range(5, 10):
    w = 9000000 + 900000 + 90000 + 5000 + 500 + (i*10) + 7
    sd = []
    for j in range(2, (int)(w**0.5)+1):
        if (w % j == 0) and (j**2 != w):
            sd.append(j)
            sd.append(w//j)
        if j**2 == w:
            sd.append(j)
    print(w, sum(sd) % 21)