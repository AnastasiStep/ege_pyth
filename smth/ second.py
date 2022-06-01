def summ(n, m):
    d = [j for j in range(len(n)*2)]
    j = 0
    for i in range(len(d)):
        if i % 2 == 0:
            d[i] = n[j]
        else:
            d[i] = m[j]
            j += 1
    return d

print(summ([1,2,3], [11,22,33]))