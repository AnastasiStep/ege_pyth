def F(n):
    if(n >= 1):
        return F(n - 1) - F(n - 2) + 3*n
    else:
        return 0
print(F(40))