f=open('var3/17.txt')
count=0
sm=0

n1=int(f.readline())
for s in f.readlines():
    n2=int(s)
    if n1%5==0 or n2%5==0:
        count=count+1
        sm=max(n1+n2, sm)
    n1=n2
print(count)
print(sm)