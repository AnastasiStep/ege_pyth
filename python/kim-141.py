a = pow(128, 56) + pow(32, 38) - 137

n = a
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b, b.count('1'))
