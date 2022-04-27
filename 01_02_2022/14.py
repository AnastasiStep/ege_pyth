for i in range(500000004, 500000100):
    d = 0
    p = 1
    a = []
    for j in range(2, int(i/2)+1):
        if d >= 5:
            break
        else:
            if i % j == 0:
                print(j)
                d += 1
                p *= j
                a.append(j)
    if d < 5:
        p = 0
    print(i, p)