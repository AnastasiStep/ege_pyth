for numb in range(250000,250100):
    summ = 0
    for i in range(2, numb - 1):
        l = 0
        if (numb % i == 0):
            for j in range(2, i - 1):
                if (i % j == 0):
                    l = l + 1
            if (l == 0):
                summ += i
    if (summ != 0) and (summ % 17 == 0):
        print(numb, summ)