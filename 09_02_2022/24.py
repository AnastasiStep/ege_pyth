f = open('09_02_2022/24.txt')
s = f.readline()
l = 0
print(len(s))
for i in range(len(s)):
    if s[i] == 'E':
        i += 1
        k = 0
        while s[i] != 'E' and s[i] != 'F' and i < len(s) - 1:
            k+=1
            i+=1
        if k >= 12:
            l+=1
print(l)