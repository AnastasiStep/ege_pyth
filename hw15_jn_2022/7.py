def f (x, y):
    if x == y: return 1
    elif x < y or x == 20: return 0
    else: return f(x - 1, y) + f(x - 2, y) + f(x**0.5, y)
print(f(27, 18) + f(18, 6))