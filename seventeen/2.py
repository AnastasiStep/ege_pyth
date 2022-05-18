f = open('seventeen/2.txt')
s = [i for i in f]
for p in range(0, len(s)):
    s[p] = (int)(s[p])

for i in range(0, len(s) - 1):
    