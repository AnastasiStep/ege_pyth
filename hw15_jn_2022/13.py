from numpy import diff


k = 0
for n in range(65000, 100000):
    s = str(n)
    if s[0] == '6' and s[-2] == '5' and s[1:-2].count('97') == 1:
        sd = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0 and i**2 != n:
                if i % 2 == 0:
                    sd.append(i)
                if (n//i) % 2 == 0:
                    sd.append(n//i)
            if i**2 == n:
                if i % 2 == 0:
                    sd.append(i)
        if len(sd) >= 4:
            k += 1
            print(n, sum(sd))
    if k == 7:
        break
#69750 129792
#69752 122080
#69756 139536
#69758 75152