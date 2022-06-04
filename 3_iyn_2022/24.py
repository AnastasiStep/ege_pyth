s = open('3_iyn_2022/24.txt').readline()
maxa = 0
for i in range(len(s) - 2):
    k = 0
    while ((s[i] + s[i + 1] + s[i + 2]) == 'XYZ') and (i < len(s) - 3):
        k += 3
        i += 3
    if k > maxa:
        maxa = k
print(maxa)