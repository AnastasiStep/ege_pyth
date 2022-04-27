s = open('diagnost/24.txt').readline()
l = lmax = k = 0
for c in s:
    if c != 'A':
        l += 1
        if c == 'E':
            k += 1
    else:
        if k >= 3 and l>lmax:
            lmax = l
        l = k = 0
if l >= 3 and l > lmax:
    lmax = l
print(lmax)