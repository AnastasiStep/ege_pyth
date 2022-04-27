for a in 1,0:
    for b in 1,0:
        for c in 1,0:
            for d in 1,0:
                if (a <= d) and (not(b <= c)) == 1:
                    print(a,b,c,d)
print("dabc")

for x in 1,0:
    for y in 1,0:
        for z in 1,0:
            for w in 1,0:
                if (((x <= w) or y and (not(z))) and ((y <= (not(z))) or x and (not(w)))) == 0:
                    print(x,y,z,w)
print("zwyx")

for x in 1,0:
    for y in 1,0:
        for z in 1,0:
            for w in 1,0:
                if ((x and (y or (not(z))) and w) == (x <= (not(y)) and z)) == 1:
                    print(x,y,z,w)
print("yxzw")


P = [i for i in range(20, 31)]
Q = [i for i in range(5, 16)]
R = [i for i in range(35,51)]
ans = []
lans = 0
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        flag = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
             if (((x in P) <= (x in Q)) or (not(x in A) <= (x in R))) == 0:
                 flag = 0
                 break
        if flag == 1:
            ans.append(len(A))
print(min(ans))



#22 11 330