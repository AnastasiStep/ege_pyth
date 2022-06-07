k = 0
for i in range(1000000, 10000000):
    if i % 5 == 0:
        w = (str)(i)
        if ((w.count('0') <= 1) and (w.count('1') <= 1) and (w.count('2') <= 1) 
        and (w.count('3') <= 1) and (w.count('4') <= 1) and (w.count('5') <= 1) 
        and (w.count('6') <= 1) and (w.count('7') <= 1) and (w.count('8') <= 1)
        and (w.count('9') <= 1)):
            f = 0
            for i in range(len(w) - 1):
                if (((int)(w[i]) % 2 == 0) and ((int)(w[i + 1]) % 2 == 0)) or (((int)(w[i]) % 2 != 0) and ((int)(w[i + 1]) % 2 != 0)):
                    f = 1
            if f == 0:
                k+=1
print(k)