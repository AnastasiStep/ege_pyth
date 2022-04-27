f = open('python/kim-171_test.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))
k=0
mx = 0
for i in range(len(a)-1):
    if a[i]%5==0 or a[i+1]%5 == 0:
        k+=1
        if a[i]+a[i+1] > mx:
            mx = a[i]+a[i+1]
print(k, mx)