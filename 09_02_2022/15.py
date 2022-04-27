P = [i for i in range(69, 91)]
Q = [i for i in range(77, 114)]
ans = []
lans = 0
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        flag = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
             if ((x in P) <= ((not((x in P) == (x in Q))) or ((x in Q) <= (x in A)))) == 0:
                 flag = 0
                 break
        if flag == 1:
            ans.append(len(A))
print(min(ans))