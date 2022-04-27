f = open('01_02_2022/7.txt')
s = f.readlines()
a = []
for i in range(0, len(s) - 1):
    l = 0
    k = i
    while (int(s[k]) > int(s[k + 1])) and ((k + 1) < len(s)):
        l+=1
        k+=1
    a.append(l)
print(max(a), a.count(max(a)))