def F(n):
    if n == 1:
        return 0
    else:
        return F(n - 1) + n

def G(n):
    if n == 1:
        return 0
    else:
        return G(n - 1) * n
print(F(5) + G(5))
#14