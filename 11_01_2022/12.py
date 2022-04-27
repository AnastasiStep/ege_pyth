a = 1
k = '1'
while a < 84:
    k += '1'
    a += 1

while '11111' in k:
    k = k.replace('222', '1', 1)
    k = k.replace('111', '2', 1)
print(k)