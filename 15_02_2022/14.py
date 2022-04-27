for A in range(1,1000):
    k = 0
    for x in range(0,1000):
        if (((not(x % A == 0)) and (x % 15 == 0)) <= ((not(x % 18 == 0)) or (not(x % 15 == 0)))) == 0:
            k += 1
            break
    if k == 0:
        print(A)