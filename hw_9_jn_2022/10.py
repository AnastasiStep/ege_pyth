sch = '02468'
sne = '13579'
k = 0
for i1 in sne:
    for i2 in sch:
        for i3 in sne:
            for i4 in sch:
                for i5 in sne:
                    for i6 in sch:
                        for i7 in sch:
                            w = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            if i1 != '0':
                                if (i7 == '0') or (i7 == '5'):
                                    if ((w.count('0') <= 1) and (w.count('1') <= 1) and (w.count('2') <= 1) 
                                    and (w.count('3') <= 1) and (w.count('4') <= 1) and (w.count('5') <= 1) 
                                    and (w.count('6') <= 1) and (w.count('7') <= 1) and (w.count('8') <= 1)
                                    and (w.count('9') <= 1)):
                                        k += 1
print(k * 2)