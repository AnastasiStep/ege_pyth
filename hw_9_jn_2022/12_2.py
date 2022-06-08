def f(s1, s2, n):
    if (s1 + s2) >= 68:
        if n == 3: return True
        else: return False
    else:
        if n >= 3: return False
        elif n % 2 != 0:
            return f(s1 + 1, s2, n + 1) and f(s1, s2 + 1, n + 1) and f(s1 + s2, s2, n + 1) and f(s1, s2 + s1, n + 1)
        else:
            return f(s1 + 1, s2, n + 1) or f(s1, s2 + 1, n + 1) or f(s1 + s2, s2, n + 1) or f(s1, s2 + s1, n + 1)


for s in range(1,60):
    if f(8, s, 0):
        print(s)