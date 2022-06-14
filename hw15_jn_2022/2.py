s = 'АЕЖЙМУ'
k = 0
l = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        k += 1
                        if k % 2 == 0:
                            w = i1 + i2 + i3 + i4 + i5 + i6
                            if (w.count('А') == 1 and w.count('Е') == 1
                            and w.count('Ж') == 1 and w.count('Й') == 1
                            and w.count('М') == 1 and w.count('У') == 1):
                                l += 1
print(l)
#360