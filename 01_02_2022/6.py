def F(n):
    if (n <= 1):
        return n
    elif (n > 1) and (n % 3 == 0):
        return n + F(n / 3)
    elif (n > 1) and (n % 3 != 0):
        return n + F(n + 3)

print(F(81))