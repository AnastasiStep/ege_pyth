def F(n):
    if n == 0:
        return 0
    else:
        if (n > 0) and (n % 2 == 0):
            return F(n//2)
        if (n > 0) and (n % 2 != 0):
            return 1 + F(n - 1)
i = 0
for a in range(0, 1001):
    if F(a) == 3:
        i += 1
print(i)