a = pow(6, 54) + pow(216, 21) - 12
n = a
b = ''
while n > 0:
    b = str(n % 6) + b
    n = n // 6
print(b, b.count('5'))