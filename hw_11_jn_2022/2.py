s = 'ОБЩЕСТВ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    w = i1 + i2 + i3 + i4 + i5
                    if i1 != 'Щ'  and i1 != 'Б':
                        if (i4 + i5) == 'ВВ':
                            if ('ЕВ' not in w) and ('ВЕ' not in w) and ('ТБ' in w):
                                k += 1
print(k)