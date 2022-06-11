def f(s1, s2, n):
    if (s1 + s2) >= 47 and (s1 + s2) <= 59:
        if n == 3:
            return True
        else:
            return False
    elif s1 + s2 > 59:
        if n == 2:
            return True
        else: return False
    else:
        if n >= 3:
            return False
        elif n % 2 != 0:
            return f(s1 + 2, s2, n + 1) and f(s1, s2 + 2, n + 1) and f(s1 * 3, s2, n + 1) and f(s1, s2 * 3, n + 1)
        else:
            return f(s1 + 2, s2, n + 1) or f(s1, s2 + 2, n + 1) or f(s1 * 3, s2, n + 1) or f(s1, s2 * 3, n + 1)

for s in range(1, 41):
    if f(5, s, 0):
        print(s)