P = [i for i in range(19,85)]
Q = [i for i in range(4,52)]
ans = []
for Amin in range(0,100):
    for Amax in range(Amin + 1, 101):
        f = 0
        A = [i for i in range(Amin, Amax)]
        for x in range(0,100):
            if ((x in P) <= ((not(x in Q)) <= (not((x in P) and (not(x in A)))))) == 0:
                f = 1
                break
        if f == 0:
            ans.append(len(A))
print(min(ans))