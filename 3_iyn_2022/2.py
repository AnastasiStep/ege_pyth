for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            for d in 0,1:
                if (((not(b <= a)) and (c <= d)) != (a and b and c and (not(d)))) == 1:
                    print(a, b, c, d)