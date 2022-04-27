f = open('fr/27-A.txt')
n = int(f.readline())

s = 0
k = 0
s1 = [10**20]*10
ms = 0

for i in range(n):
    x = int(f.readline())
    s+=x
    if x%2!=0: k+=1
    if k%10==0: ms = s
    elif s1[k%10]!=10**20:
        ms = max(ms, s-s1[k%10])

    s1[k%10] = min(s1[k%10],s)
print(ms)