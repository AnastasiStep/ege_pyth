for i in range(174457, 174505):
    a = []
    for j in range(2, i):
        if i % j == 0:
            a.append(j)
    if len(a) == 2:
        print(a)