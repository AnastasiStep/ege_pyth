def f(s, n):
    if s <= 1:
        if (n == 2) or (n == 4): return True
        else: return False
    else:
        if n >= 4: return False
        elif n % 2 == 0:
            if (s % 3 == 0) and (s % 2 == 0):
                return f(s/2, n + 1) and f((s*2)/3, n + 1)
            elif s % 3 == 0:
                return f(s/3, n + 1) and f(s - 2, n + 1)
            elif s % 2 == 0:
                return f(s/2, n + 1) and f(s - 3, n + 1)
            else:
                return f(s - 3, n + 1) and f(s - 2, n + 1)
        else:
            if (s % 3 == 0) and (s % 2 == 0):
                return f(s/2, n + 1) or f((s*2)/3, n + 1)
            elif s % 3 == 0:
                return f(s/3, n + 1) or f(s - 2, n + 1)
            elif s % 2 == 0:
                return f(s/2, n + 1) or f(s - 3, n + 1)
            else:
                return f(s - 3, n + 1) or f(s - 2, n + 1)

def g(s,n):
    if s <= 1:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0:
            if (s % 3 == 0) and (s % 2 == 0):
                return g(s/2, n + 1) and g((s*2)/3, n + 1)
            elif s % 3 == 0:
                return g(s/3, n + 1) and g(s - 2, n + 1)
            elif s % 2 == 0:
                return g(s/2, n + 1) and g(s - 3, n + 1)
            else:
                return g(s - 3, n + 1) and g(s - 2, n + 1)
        else:
            if (s % 3 == 0) and (s % 2 == 0):
                return g(s/2, n + 1) or g((s*2)/3, n + 1)
            elif s % 3 == 0:
                return g(s/3, n + 1) or g(s - 2, n + 1)
            elif s % 2 == 0:
                return g(s/2, n + 1) or g(s - 3, n + 1)
            else:
                return g(s - 3, n + 1) or g(s - 2, n + 1)

for s in range(1,38):
    if f(s,0) == True and g(s,0) == False:
        print(s)