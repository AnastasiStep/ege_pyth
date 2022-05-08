P = [i for i in range(5, 31)]
Q = [i for i in range(14, 24)]
ans = []
for Amin in range(0,100):
    for Amax in range(Amin + 1, 101):
        flag = 0
        A = [i for i in range(Amin, Amax)]
        for x in range(0,100):
            if (((x in P) == (x in Q)) <= (not(x in A))) == 0:
                flag = 1
                break
        if (flag == 0):
            ans.append(len(A))
print(max(ans))