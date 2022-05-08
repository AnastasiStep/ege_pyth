for A in range(0,100):
    f = 0
    for x in range(0,100):
        for y in range(0,100):
            if (((x <= 9) <= (x*x <= A)) and ((y*y <= A) <= (y <= 9))) == 0:
                f = 1
                break
    if f == 0:
        print(A)