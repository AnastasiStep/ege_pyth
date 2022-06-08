s = '01234'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    w = i1 + i2 + i3 + i4 + i5
                    if i1 != 0:
                        if w.count('2') + w.count('4') + w.count('0') <= 3:
                            k+=1
print(k)