def f(x, y, k):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x < y:
        if k == 0:
            return f(x + 1, y, 0) + f(x + 2, y, 0) + f(x * 2, y, 1)
        else:
            return f(x + 1, y, 0) + f(x + 2, y, 0)
print(f(1, 9, 0))