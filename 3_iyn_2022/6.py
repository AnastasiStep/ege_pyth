for x in range(0,1000):
    s = x
    n = 12
    while s > 0:
        s = s - 10
        n = n + 7
    if n == 61:
        print(x)