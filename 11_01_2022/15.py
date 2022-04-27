x = 0
y = 0
a = 0
k = 0

for a in range(0, 1000):
    k = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((((x <= 9) <= (x*x <= a)) and ((y*y <= a) <= (y <= 9))) == 0):
                k += 1
                break
    if (k == 0):
        print(a)