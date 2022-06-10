def f(s, h, n):
    if s >= 140:
        if n == 3: return True
        else: return False
    else:
        if n >= 3: return False
        elif n % 2 != 0:
            if h == 1: return f(s + 2, 2, n + 1) and f(s * 3, 3, n + 1)
            elif h == 2: return f(s + 1, 1, n + 1) and f(s * 3, 3, n + 1)
            elif h == 3: return f(s + 1, 1, n + 1) and f(s + 2, 2, n + 1)
            else: return f(s + 1, 1, n + 1) and f(s + 2, 2, n + 1) and f(s * 3, 3, n + 1)
        else:
            if h == 1: return f(s + 2, 2, n + 1) or f(s * 3, 3, n + 1)
            elif h == 2: return f(s + 1, 1, n + 1) or f(s * 3, 3, n + 1)
            elif h == 3: return f(s + 1, 1, n + 1) or f(s + 2, 2, n + 1)
            else: return f(s + 1, 1, n + 1) or f(s + 2, 2, n + 1) or f(s * 3, 3, n + 1)

for s in range(1, 140):
    if f(s, 0, 0):
        print(s)