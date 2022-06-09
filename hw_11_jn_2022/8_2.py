def f1(s1, s2, n):
    if (s1 + s2) >= 47:
        if n == 3:
            return True
        else:
            return False
    else:
        if n >= 3:
            return False
        elif n % 2 != 0:
            return f1(s1 + 2, s2, n + 1) and f1(s1, s2 + 2, n + 1) and f1(s1 * 3, s2, n + 1) and f1(s1, s2 * 3, n + 1)
        else:
            return f1(s1 + 2, s2, n + 1) or f1(s1, s2 + 2, n + 1) or f1(s1 * 3, s2, n + 1) or f1(s1, s2 * 3, n + 1)

for s in range(1, 41):
    if f1(5, s, 0):
        print(s)