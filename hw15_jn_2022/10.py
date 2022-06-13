def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else: return f(x + 3, y) + f(x * 3, y)
k = 0
for i in range(4, 100):
    if f(3, i) != 0:
        k += 1
print(k)