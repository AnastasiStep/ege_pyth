for i in range(0,100000):
    x = i
    a = 0
    b = 0
    while x > 0:
        a+=1
        if x % 2 == 0:
            b += x % 100
        x//=10
    if a == 4 and b == 142:
        print(i)