f = open('demo/12.txt')
s = f.readlines()
a = []
for i in s:
    a.append(int(i))

k = 0;
suma = a[0] + a[1]

for i in range(len(a)-1):
    if (a[i] % 5 == 0 or a[i+1] % 5 == 0):
        k+=1
        if ((a[i] + a[i+1]) < suma):
            suma = a[i] + a[i+1]
print(k, suma)