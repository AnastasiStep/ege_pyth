n = 50
while (n < 81):
    x = n
    b = ''
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    print(n, b)
    n = n + 1