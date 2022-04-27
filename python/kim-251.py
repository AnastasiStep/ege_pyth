n = 120000
while (n < 220000):
    if (n % 125 == 0):
        n1 = n
        suma = 0
        while n1 > 0:
            digit = n1 % 10
            if (digit % 2 != 0):
                suma = suma + 1
            n1 = n1 // 10
        if (suma == 3):
            print(n)
    n = n + 1