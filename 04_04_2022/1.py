n = 18
b = ''
while n > 0:
    b = str(n % 3) + b
    n = n // 3
print(b)