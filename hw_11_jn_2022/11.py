for i in range(19500000, 19500100):
    sd = []
    for j in range(2, (int)(i**0.5)+1):
        if (i % j == 0) and (j**2 != i):
            f = 0
            for k in range(2, (int)((i//j)**0.5)+1):
                if (i//j) % k == 0:
                    f += 1
                    break
            if f > 0:
                break
            else:
                print(i, i // j)
                break
        if j**2 == i:
            f = 0
            for k in range(2, (int)(j**0.5)+1):
                if j % k == 0:
                    f += 1
                    break
            if f > 0:
                break
            else:
                print(i)