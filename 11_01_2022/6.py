x = 0
while x < 1000:
    s = x
    s = s // 10
    n = 1
    while s < 51:
        s = s + 5
        n = n * 2
    if (n == 64):
        print(x, n)
    x += 1