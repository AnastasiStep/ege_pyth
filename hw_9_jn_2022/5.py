s = 'ЗАПИСЬ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        w = i1 + i2 + i3 + i4 + i5 + i6
                        if ((w.count('З') == 1) and (w.count('А') == 1) and (w.count('П') == 1) 
                        and (w.count('И') == 1) and (w.count('С') == 1) and (w.count('Ь') == 1)):
                            if (i1 != 'Ь') and ('ИЬ' not in w) and ('АЬ' not in w):
                                k += 1
print(k)