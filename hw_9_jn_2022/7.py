sg = 'ОАИ'
ss = 'ЛГРФМ'
k = 0

for i4 in ss:
    for i5 in sg:
        for i1 in ss:
            for i2 in sg:
                for i3 in ss:
                    w = i1 + i2 + i3 + i4 + i5
                    if len(set(w)) == 5:
                        k += 1
print(k)