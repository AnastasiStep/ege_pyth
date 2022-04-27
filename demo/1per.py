for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (not (x and y) and (y or z) or not w) == 0:
                    print(x, y, z, w)
#ywzx