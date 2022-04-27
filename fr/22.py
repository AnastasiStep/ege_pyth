from re import A


for c in range(0,1000):
    x = c
    a = 7*x+27
    b = 7*x-33
    while a != b:
        if a > b:
            a-=b
        else:
            b-=a
    if(a == 10):
        print(c, a)