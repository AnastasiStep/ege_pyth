for i in range(400000000, 600000000):
    n = 1
    m = 0
    while pow(2, m)*pow(3, n) <= i:
        while pow(2, m)*pow(3, n) <= i:
            if pow(2, m)*pow(3, n) == i:
                print(pow(2, m)*pow(3, n), i)
            m+=2
        m = 0
        n+=2