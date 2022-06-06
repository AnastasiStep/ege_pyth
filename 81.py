s = 'АВТОР'
sg = 'АО'
ss = 'ВТР'
k = 0
for i1 in sg:
    for i2 in ss:
        for i3 in sg:
            for i4 in ss:
                for i5 in sg:
                    for i6 in ss:
                        for i7 in sg:
                            for i8 in ss:
                                w = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
                                if ((w.count('А') == 2) and (w.count('О') == 2) and ((w.count('Т') == 2)) 
                                and (w.count('В') == 1) and (w.count('Р') == 1)):
                                    k += 1
print(2 * k)