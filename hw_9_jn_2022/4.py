s = 'АВДПР'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                k += 1
                w = i1 + i2 + i3 + i4
                if w == 'ВДПР':
                    print(k, w)
                    break