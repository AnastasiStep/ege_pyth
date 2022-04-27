n = 3*pow(125, 6) + 2*pow(25,9) + pow(5,12) - 625
 
b = ''
 
while n > 0:
    b = str(n % 5) + b
    n = n // 5
 
print(b)