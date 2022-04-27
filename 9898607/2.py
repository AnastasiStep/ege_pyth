for x in 1,0:
    for y in 1,0:
        for z in 1,0:
            for w in 1,0:
                if ((x and (not(y))) or (x == z) or (not(w))) == 0:
                    print(x, y, z, w)