for i in range(0, 100):
    x = i
    a = 0
    b = 0
    while x > 0:
        a += 1
        if (b < (x % 8)):
            b =x % 8
        x //=  8
    if (a == 3) and (b == 2):
        print(i, a, b)
    #66