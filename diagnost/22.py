for i in range(225000000, 226000000):
    x = i
    a = 1
    b = 0
    while x > 0:
        d = x%9
        a *= d
        if d < 5:
            b += d
        x //= 9
    if a == 10 and b == 9:
        print(i)