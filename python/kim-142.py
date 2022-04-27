a = pow(9, 54) + pow(81, 21) - 54
n = a
b = ''
while n > 0:
    b = str(n % 9) + b
    n = n // 9
print(b, b.count('8'))
