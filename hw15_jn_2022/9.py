def f(x, s, u, y):
    if x == y:
        if u > s: return 1
        else: return 0
    elif x > y: return 0
    else: return f(x + 1, s + 1, u, y) + f(x * 2, s, u + 1, y) + f(x * 5, s, u + 1, y)
print(f(3, 0, 0, 260))