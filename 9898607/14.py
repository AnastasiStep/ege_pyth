n = 30
 
b = ''
 
while n > 0:
    b = str(n % 4) + b
    n = n // 4
 
print(b)