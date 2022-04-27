f = open('9898607/24.txt')
s = f.readline()
k = ''

for i in range(len(s) - 2):
    if (s[i] == s[i + 1]):
        k+=s[i+2]
maxi = 0
m = ''

for i in range(ord('A'), ord('Z')):
    if k.count(chr(i)) > maxi:
        maxi = k.count(chr(i))
        m = chr(i)
print(m)