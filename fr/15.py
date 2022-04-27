b = 0
for A in range(0, 1000):
    b = 0
    for x in range(0, 1000):
        if ((x&105 == 0) <= ((x&58!=0) <= (x&A!=0))) != 1:
            b += 1
            break
    if (b == 0):
        print(A)