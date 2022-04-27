f = open('fr/24.txt')
s = f.readline()
sub = s.split('D')
m = 0

for i in range(len(sub) - 1):
    s1=sub[i] + 'D' + sub[i+1]
    m = max(m, len(s1))
print(m)