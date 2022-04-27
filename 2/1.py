for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if (((not(x) and y and z)) or ((not(x)) and (not(y)) and z) or ((not(x)) and (not(y)) and (not(z)))) == 1:
                print(x,y,z)

#zxy
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (x and not(y) and (not(z) or w)) == 1:
                    print(x,y,z,w)

#xywz
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if ((x <= y) and (y <= z)) == 1:
                print(x,y,z)

#zyx
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            print(x, y, z, (not(z)) and x or x and y)

#zyx
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            print(x,y,z, (not(z)) and x)

#zyx
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if ((x or y) <= (z == x)) == 0:
                print(x,y,z)

#xzy
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if ((x == z) or (x <= (y and z))) == 0:
                print(x,y,z)

#yzx
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if ((x == y) or ((y or z) <= x)) == 0:
                print(x,y,z)

#zyx
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and not(y)) or (y == z) or (not(w))) == 0:
                    print(x,y,z,w)

#wzyx
print()

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x == (w or y)) or ((w <= z) and (y <= w))) == 0:
                    print(x,y,z,w)

#yxzw