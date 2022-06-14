def f(x, y):
    if x == y: return 1
    elif x > y: return 0
    else:
        #return f(x + 1, y) + f(int(str(x) + '1') if int(str(x) + '1') % 3 == 0 else x, y) + f(x * 5, y)
        return f(x + 1, y) + f((int(str(x) + '1'), x)[x % 3 == 0], y) + f(x * 5, y)
print(f(1, 140))
#???