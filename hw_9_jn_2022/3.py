s = 'КАЛИЙ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        w = i1 + i2 + i3 + i4 + i5 + i6
                        if (i1 != 'Й') and (i6 != 'Й') and ('ИЙ' not in w) and ('ЙИ' not in w) and (w.count('Й') <= 1):
                            k += 1
print(k)