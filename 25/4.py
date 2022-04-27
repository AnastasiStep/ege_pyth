for i in range(185311, 185330):
    a = []
    for j in range(1, i+1):
        if i % j == 0:
            a.append(j)
    if len(a) == 4:
        print(a)