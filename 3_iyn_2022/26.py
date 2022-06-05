f = open('3_iyn_2022/26.txt')
n = (int)(f.readline())
s = f.readlines()
for i in range(len(s)):
    s[i] = (int)(s[i])
k = 0
mina = 10000000
for i in range(n):
    for j in range(n):
        if (s[i] + s[j]) % 2 == 0:
            mino = 10000000
            sr = (s[i] + s[j])//2
            for o in range(n):
                if (s[o] - sr < mino) and (s[o] - sr > 0):
                    mino = s[o] - sr
            print(mino)
            if mino == 5:
                k+=1
print(k, mina)