f = open('11.txt')
data = f.readlines()
 
s = data[0].split()
s = int(s[0])
del(data[0])
for i in range(0, len(data)):
    if (int(data[i]) > 200):
        data[i]=int(data[i])
data=sorted(data)