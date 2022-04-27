for A in range(1,101):
    k = 0
    for x in range(0,100):
        for y in range(0,100):
            if (((2*y + x) != 65) or (x < 2*y) or (A < 3*x)) == 0:
                k = 1
                break
    if k == 0:
        print(A)