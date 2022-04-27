k = 0
for x in range(1,1000):
    s = x
    s = 3*(s//10)
    n = 1
    while s < 221:
        s = s + 13
        n = n * 2
    if n == 265:
        k+=1
print(k)