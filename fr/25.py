for x in range(500000001,500000100):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x%i==0:
            d|={i,x//i}
    if len(d)>=5:
        d=sorted(d)[:5]
        p = 1
        for i in d: p*=i
        if p<x:
            print(p)