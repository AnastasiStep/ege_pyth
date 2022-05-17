def F(n):
    if n == 0:
        return 0
    if (n > 0) and (n % 3 == 2):
        return F(n - 1) + 1
    if (n > 0) and (n % 3 < 2):
        return F((n - (n % 3))//3)
for i in range(0,1000):
    if F(i) == 6:
        print(i)
#728