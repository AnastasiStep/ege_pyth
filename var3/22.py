for i in range(0, 100):
    L = 10
    M = 0
    x = i
    while x > 0:
        y = x % 10
        x = x // 10
        if y < L:
            L = y
        if y > M:
            M = y
    if (L == 5 and M == 5):
        print(i, L, M)