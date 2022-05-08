P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
ans = []
for Amin in range(0,100):
    for Amax in range(Amin + 1, 101):
        f = 0
        A = [i for i in range(Amin, Amax)]
        for x in range(0,100):
            if (((x in A) <= (x in P)) and ((x in Q) <= (not(x in A)))) == 0:
                f = 1
                break
        if f == 0:
            ans.append(len(A))
print(A)