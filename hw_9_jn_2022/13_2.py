def f(s,n):
    if s <= 1:
        if n == 3: return True
        else: return False
    else:
        if n >= 3: return False
        elif n % 2 != 0:
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
for s in range(1,38):
    if f(s,0) == True:
        print(s)
#7 15