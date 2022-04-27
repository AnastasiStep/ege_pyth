def M(a):
    d=2
    while d*d<=a:
        if a%d==0:
            return d+(a//d)
        d+=1
    return 0
k = 0
for i in range(1000000, 1300000):
    if M(i)%10 == 0:
        k+=1
        print(i, M(i))
    if k==5:
        break