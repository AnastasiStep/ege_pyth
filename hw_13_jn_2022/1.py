s = '01234567'
k = 0
for i2 in s:
    for i3 in s:
        for i4 in s:
            for i5 in s:
                w = '7' + i2 + i3 + i4 + i5
                if int(w) % 2 == 0 and ('65' in w or '56' in w) and not('65' in w and '56' in w):
                    k += 1
print(k)