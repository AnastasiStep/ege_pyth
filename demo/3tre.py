i = 0

while i < 1000:
    s = i
    n = 1 
    while s < 45: 
        s = s + 6 
        n = n * 4 
    i+=1
    if (n == 256):
        print(i, n)
#27