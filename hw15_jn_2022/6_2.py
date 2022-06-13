def f(s, h, n):
    if s >= 20:
        if n == 3: return True
        else: return False
    else:
        if n >= 3: return False
        elif n % 2 != 0:
            if h == 0:
                if (s * 2 * 2 >= 20) or ((s + 2) * 2 >= 20) or (s * 2 + 2 >= 20) or ((s + 2) + 2 >= 20):
                    h = 1
                    return f(s, h, n + 1)
                else:
                    return f(s * 2, h, n + 1) and f(s + 2, h, n + 1)
            else:
                return f(s * 2, h, n + 1) or f(s + 2, h, n + 1)
        else:
            if h == 0:
                if (s * 2 * 2 >= 20) or ((s + 2) * 2 >= 20) or (s * 2 + 2 >= 20) or ((s + 2) + 2 >= 20):
                    h = 1
                    return f(s, h, n + 1)
                else:
                    return f(s * 2, h, n + 1) or f(s + 2, h, n + 1)
            else:
                return f(s * 2, h, n + 1) or f(s + 2, h, n + 1)
for s in range(1, 20):
    if f(s, 0, 0):
        print(s)