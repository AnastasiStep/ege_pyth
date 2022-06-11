s = '0123456789ABCDEF'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        if (i1 != '1') and ((i5 + i6) == 'AB') and (i1 != '0'):
                            k += 1
print(k)