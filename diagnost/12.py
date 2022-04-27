for i in range(201, 300):
    n = '1' * i
    while '1111' in n:
        if '1111' in n:
            n = n.replace('1111', '22', 1)
        if '222' in n:
            n = n.replace('222', '1', 1)
    print(i, n.count('1'))