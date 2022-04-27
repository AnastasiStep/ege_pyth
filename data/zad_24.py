f = open('data/dla_zad_24.txt')
s = f.readline()
k = 1
maxa = 0
i = 1
d = 0
a = 0
while i < len(s) - 2:
    k = 0
    j = i
    while (ord(s[j]) < ord(s[j + 1])) and (j < len(s) - 2):
        #print(s[i])
        k += 1
        j += 1
    #print('----', i, k)
    if (k > maxa):
        maxa = k
        d = k
        a = i
    i += 1
print(a + 1)