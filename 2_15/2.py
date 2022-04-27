for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x <= y)and((x<=z)==(y<=x))) == 1:
                    print(x,y,z,w)

print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x or y) and (not(y == z)) and (not(w))) == 1:
                    print(x,y,z,w)

P = [i for i in range(5, 111)]
Q = [i for i in range(15, 43)]
R = [i for i in range(25, 71)]
ans = []
lans = 0
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        flag = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
             if (((x in P) <= (x in Q)) or ((not(x in A)) <= (not(x in R)))) == 0:
                 flag = 0
                 break
        if flag == 1:
            ans.append(len(A))
print(min(ans))

P = [i for i in range(15, 31)]
Q = [i for i in range(5, 61)]
ans = []
lans = 0
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        flag = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
             if (((not(x in Q)) or (x in P)) and (x in A)) == 1:
                 flag = 0
                 break
        if flag == 1:
            ans.append(len(A))
print(max(ans))

i = 0
for A in range(1,10000):
    k = 0
    for x in range(0,100):
        if ((A % 5 == 0) and (not(2020 % A == 0)) <= ((x % 1718 == 0) <= (2023 % A == 0))) == 0:
            k = 1
            break
    if k == 0:
        i+=1
print(i)

for A in range(1,101):
    k = 0
    for x in range(0,100):
        if ((x & 41 == 0) <= ((x & 119 != 0) <= (x & A != 0))) == 0:
            k = 1
            break
    if k == 0:
        break
print(A)

for A in range(1,101):
    k = 0
    for x in range(0,100):
        for y in range(0,100):
            if (((x - 20 < A) and (20 - x < A)) or (x*y > 50)) == 0:
                k = 1
                break
    if k == 0:
        break
print(A)

for A in range(1,101):
    k = 0
    for x in range(0,100):
        for y in range(0,100):
            if ((5*x + 3*y != 60) or ((A > x) and (A > y))) == 0:
                k = 1
                break
    if k == 0:
        break
print(A)















#а тебя когданибудь заебывали все люди на свете. 
# Прям все все... 
# И виной всему этому всего один гребаный человек... 
# Приколько... Ведь этому человеку мне еще надо поарить подарок... 
# Ска как я ненавижу эту жизнь... Мда... 
# Почему все на этом свете считают что со мной чтото не так?? 
# Я этого не понимаю почему нельзя просто отстать от человека
#Господи люди я просто хочу отдохнуть от вас что вы ко мне привязались?!