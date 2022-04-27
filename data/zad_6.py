a = 0
while a <= 1000:
    s = a
    n = 1
    while s < 200:
        s = s + 25
        n = n * 2
    if (n == 64):
        print(a, n)
    a = a + 1
