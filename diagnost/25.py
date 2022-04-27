def delitels(n):
    dels = []
    for i in range(2, n - 1):
        if n % i == 0:
            dels.append(i)
    if dels:
        return dels[-1] + dels[-2]
    return 0
count = 0
for i in range(10000001, 10000000000):
    if 0 < delitels(i) < 10000:
        count += 1
        print(delitels(i))
    if count == 5:
        break