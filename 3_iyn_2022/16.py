def F(n):
    if n == 1:
        return 1
    else:
        if n >= 2:
            if n % 2 == 0:
                return F(n/2) + 1
            else:
                return F(n - 1) + n
for i in range(0,1000):
    if F(i) == 19:
        print(i)