a = 1
k = '1'
while a < 98:
    k += '1'
    a += 1

while '1111' in k:
    k = k.replace('1111', '22', 1)
    k = k.replace('222', '1', 1)
print(k)