from itertools import count


k = 0
for n in range(16606, 10000000):
    s = str(n)
    if s[1] == '6' and s[-1] == '6' and s[2:-2].count('6') >= 1:
        if (n % 6 == 0) and (n % 7 == 0) and (n % 8 == 0):
            k += 1
            sd = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0 and i**2 != n:
                    sd.append(i)
                    sd.append(n//i)
                if i**2 == n:
                    sd.append(i)
            print(n, sum(sd))
    if k == 7:
        break