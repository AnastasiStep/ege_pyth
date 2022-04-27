for x in 1,0:
    for y in 1,0:
        for z in 1,0:
            for w in 1,0:
                if ((not(z) == y) <= ((w and (not(x))) == (y and x))) == 0:
                    print(x, y, z, w)