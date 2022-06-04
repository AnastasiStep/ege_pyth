P = [i for i in range(10, 25)]
Q = [i for i in range(15,30)]
R = [i for i in range(25,40)]
ans = []
lans = 0
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        flag = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
             if (((x in Q) <= (not(x in R))) and (x in A) and (not(x in P))) == 1:
                 flag = 0
                 break
        if flag == 1:
            ans.append(len(A))
print(max(ans))