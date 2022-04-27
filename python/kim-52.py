x = 2
while (x < 1000):
    n = x
    if (n % 3 == 0):
        n = n / 3
    else:
        n = n - 1
    if (n % 5 == 0):
        n = n / 5
    else:
        n = n - 1
    if (n % 11 == 0):
        n = n / 11
    else:
        n = n - 1
    if (n == 8):
        print(n, x)
    x = x + 1