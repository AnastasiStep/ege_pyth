import math
def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n/i])
    divs.extend([n])
    return len(list(set(divs)))

for i in range(460000000, 460001000):
    if divisors(i) >= 5:
        print(i)