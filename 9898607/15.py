b = 0
for A in range(0, 1000):
    b = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((x*y < A) or (x < y) or (x >= 12)) != 1:
                b += 1
                break
    if (b == 0):
        print(A)