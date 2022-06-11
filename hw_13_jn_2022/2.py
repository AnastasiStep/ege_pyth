sg = 'ЕО'
ss = 'ВРТН'
k = 0
for i1 in ss:
    for i2 in sg:
        for i3 in ss:
            for i4 in sg:
                for i5 in ss:
                    for i6 in sg:
                        for i7 in ss:
                            for i8 in sg:
                                w = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
                                if (w.count('Е') == 3 and w.count('О') == 1
                                and w.count('В') == 1 and w.count('Р') == 1
                                and w.count('Т') == 1 and w.count('Н') == 1):
                                    k += 1
print(k * 2)