s = '012345678'
k = 0
for i1 in s:
    for i2 in s:
        for i3 in s:
            for i4 in s:
                for i5 in s:
                    for i6 in s:
                        for i7 in s:
                            if i1 != '0':
                                if i1 != '2' and i1 != '4' and i1 != '6':
                                    if i7 != i6 or i6 != i5: # не могут быть равны все три, а, например, 6ой и 5ый могут быть равны
                                        k += 1
print(k)
#2099520
