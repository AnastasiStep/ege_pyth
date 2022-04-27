f = open('26/8.txt')
s = f.readline()
a = s.split()
k = (int)(a[0])
l = (int)(a[1])
s = f.readlines()
#print(l,k)
for i in range(l):
    s[i] = (int)(s[i])
data = sorted(s,reverse=True) # или data.sort(reverse = True)
summa = 0
 
for i in range(0,l):
    summa+=s[i]*0.2 # 10000 10000 10000
print(s[l],int(summa))
