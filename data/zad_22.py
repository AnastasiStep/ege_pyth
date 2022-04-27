a = -1000
while a <= 1000:
    x = a
    P = 0
    S = 10*(x - x % 15)
    i = 2
    while i < 20:
        S = S - 2*i
        P = P + i
        i = i + 2
    
    if (S == 270 and P == 90):
        print(a, S, P)
    a += 1