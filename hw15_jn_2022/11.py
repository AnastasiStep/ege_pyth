def f(x, d, y):
    if x == y: return d
    elif x > y: return 0
    else: return f(x + 1, d + 1, y) + f(x * 2, d + 1, y) + f(x + (x % 4), d + 1, y)
k = 0
for i in range(1, 1000):
    if f(i, 0, 80)<= 5:
        k += 1
print(k)