s = 'ПСКАЛЬ'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                w = i1 + i2 + i3 + i4
                if (i1 != 'Ь') and ('ЬЬ' not in w):
                    k += 1
print(k)
