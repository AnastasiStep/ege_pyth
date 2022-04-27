for i in range(210235, 210300):
    a = []
    for j in range(2, i):
        if i % j == 0:
            a.append(j)
    if len(a) == 4:
        print(a)