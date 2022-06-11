k = 0
for n in range(300000000, 0, -1):
    sd = []
    for i in range(2, int(n**0.5) + 1):
        if (i**2 != n) and (n % i == 0):
            u = 0
            t = i
            while t > 0:
                m = t % 10
                t = t//10
                if m % 2 == 0:
                    u = 1
                    break
            if u == 0:
                sd.append(i)
            u = 0
            t = n//i
            while t > 0:
                m = t % 10
                t = t//10
                if m % 2 == 0:
                    u = 1
                    break
            if u == 0:
                sd.append(n//i)
        if i**2 == 0:
            u = 0
            t = i
            while t > 0:
                m = t % 10
                t = t//10
                if m % 2 == 0:
                    u = 1
                    break
            if u == 0:
                sd.append(i)
    if len(sd) > 5:
        k += 1
        sd = sd[::-1]
        print(sd[4], len(sd))
    if k == 5:
        break