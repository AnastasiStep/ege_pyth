def F(n):
    if n == 0:
        return 0
    elif n > 0:
        if n % 2 == 0:
            return F(n/2)
        else:
            return 1 + F(n - 1)
k = 0
for i in range(1, 900):
    if(F(i)==9):
        k+=1
print(k)