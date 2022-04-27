a = 1
k = '1'
while a < 206:
    k += '1'
    a += 1

while '111' in k or '222' in k:
    k = k.replace('111', '22', 1)
    k = k.replace('222', '1', 1)
print(k)