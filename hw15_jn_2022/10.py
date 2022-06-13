def f(x, d, y):
    if x == y:
        if d <= 5: return 1
        else: return 0
    elif x > y: return 0
    else: return f(x + 1, d + 1, y) + f(x * 2, d + 1, y) + f(x + (x % 4), d + 1, y)
for i in range(1, 1000):
    if f(i, 0, 80) != 0:
        print(f(i, 0, 80))