for i in range(2,1000):
    n = i
    sch = 0
    while n > 0:
        if n % 10 % 2 == 0:
            sch += n % 10
        n = n // 10
    n = str(i)
    s = 0
    for j in range(len(n)):
        if ((j + 1) % 2 == 0):
            s += int(n[j])
        if (abs(s - sch) == 9):
            print(i)