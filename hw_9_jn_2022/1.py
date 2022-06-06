s = 'МИКРЯ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        for i7 in s:
                            for i8 in s:
                                w = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8
                                if ((w.count('М') == 2) and (w.count('И') == 3) and (w.count('К') == 1) and (w.count('Р')) == 1 and (w.count('Я'))) == 1:
                                    k += 1
print(k)