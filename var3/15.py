def F(n):
    if (n == 0) or (n == 1):
        return 1;
    elif (n % 2 == 0):
        return n + F(n - 1)
    elif (n > 1) and (n % 2 != 0):
        return n+ F(n - 3)
print(F(14))