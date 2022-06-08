sg = 'ОАИ'
ss = 'ЛГРФМ'
k = 0
for i5 in sg:
    for i1 in ss:
        for i2 in sg:
            for i3 in ss:
                for i4 in sg:
                    w = i1 + i2 + i3 + i4 + i5
                    if ((w.count('Л') <= 1) and (w.count('Г') <= 1) and (w.count('Р') <= 1) 
                    and (w.count('Ф') <= 1) and (w.count('М') <= 1) and (w.count('О') == 1) 
                    and (w.count('А') == 1) and (w.count('И') == 1)):
                        k += 1
print(k)