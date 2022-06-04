f = open('3_iyn_2022/26.txt')
n = (int)(f.readline())
s = f.readlines()
for i in range(len(s)):
    s[i] = (int)(s[i])
k = 0
mina = 10000000
for i in range(n):
    for j in range(n):
        if i != j:
            sr = (s[i] + s[j])//2
            print(s[i], s[j], sr, s[i] - sr, s[j] - sr)
            if (s[i] - sr == 5) or (s[j] - sr == 5):
                k += 1
                if sr < mina:
                    mina = sr
print(k, mina)