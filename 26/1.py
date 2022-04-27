f = open('26/1.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del(data[0])
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for k in range (0,len(data)):
    if summa + data[k] > s: break
    summa += data[k]
print (k)
zapas = s - summa
for i in range (0,len(data)):
    if data[i] - data[k-1] <= zapas:
        itog = data[i]
print(itog)