s = '012345678'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i3 in s:
                for i4 in s:
                    for i5 in s:
                        for i6 in s:
                            w = i1 + i2 + i3 + i4 + i5 + i6
                            if i1 != 0:
                                if (i1 != 3) and (i1 != 7):
                                    if ((w.count('00') == 0) and (w.count('11') == 0)
                                    and (w.count('22') == 0) and (w.count('33') == 0)
                                    and (w.count('44') == 0) and (w.count('55') == 0)
                                    and (w.count('66') == 0) and (w.count('77') == 0)
                                    and (w.count('88') == 0)):
                                        k += 1
print(k)