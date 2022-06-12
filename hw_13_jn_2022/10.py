k = 0
for i in range(166006, 167000, 10):
    if (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0):
        k += 1
        sd = []
        for j in range(2, (int)(i**0.5)+1):
            if (i % j == 0) and (j**2 != i):
                sd.append(j)
                sd.append(i//j)
            if j**2 == i:
                sd.append(j)
        print(i, sum(sd))
for i in range(1660006, 1670000, 10):
    if (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0):
        k += 1
        sd = []
        for j in range(2, (int)(i**0.5)+1):
            if (i % j == 0) and (j**2 != i):
                sd.append(j)
                sd.append(i//j)
            if j**2 == i:
                sd.append(j)
        print(i, sum(sd))
    if k == 7:
        break