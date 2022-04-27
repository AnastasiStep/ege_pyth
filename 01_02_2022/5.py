for A in range(0,100):
    k = 0
    for x in range(0,100):
        for y in range(0,100):
            if ((x**2 - 3*x + 2 > 0) or (y > x**2 + 7) or (x*y < A)) == 0:
                k += 1
                break
    if k == 0:
        print(A)
        break