for i in range(123456789, 223456789):
    a = []
    for j in range(2, i):
        if i % j == 0:
            if len(a) > 3:
                break
            a.append(j)
    if len(a) == 3:
        print(i, max(a))