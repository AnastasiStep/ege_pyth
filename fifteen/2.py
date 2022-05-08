for A in range(0,20):
    a = 0
    for x in range(0,100):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == 0:
            a = 1
            break
    if a == 0:
        print(A)