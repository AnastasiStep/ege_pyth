def f(s,n):
    if s >= 68:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0:
            return f(s + 1, n + 1) and f(s + 4, n + 1) and f(s * 5, n + 1)
for i in range(0,100):
    print(f(i,0))