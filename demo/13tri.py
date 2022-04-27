a = 0

while (a < 1000):
    x = a
    L = 0 
    M = 0 
    while x > 0:
        M = M + 2
        if x % 8 != 0:
            L = L + 1
        x = x // 8
    if (L == 2 and M == 6):
        print(L, M, a)
    a+=1


