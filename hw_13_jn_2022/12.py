l = 0
for k in range(1, 10000):
    n = 1850000000 + k
    sd = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0 and i**2 != n:
            if i % 2 == 0:
                sd.append(i)
            if n//i % 2 == 0:
                sd.append(n//i)
        if i**2 == n:
            if i % 2 == 0:
                sd.append(i)
    if len(sd) % 2 != 0:
        l += 1
        print(k, len(sd))
    if l == 5:
        break