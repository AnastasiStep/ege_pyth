for i in range(35819640, 40000000):
    k = 0
    for j in range(1, i + 1):
        if (j % 2 != 0):
            if (i % j == 0):
                k+=1
    if (k == 5):
        print(i)