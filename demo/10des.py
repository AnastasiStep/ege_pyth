a = pow(64, 9) + pow(8, 25) - 9

n = a
 
b = ''
 
while n > 0:
    b = str(n % 8) + b
    n = n // 8
 
print(b)