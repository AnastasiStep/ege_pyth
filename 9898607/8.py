a = ['Г', 'О', 'Д']
k = 0
for s1 in a:
    for s2 in a:
        for s3 in a:
            for s4 in a:
                for s5 in a:
                    for s6 in a:
                        if ((s1 == 'Г' or s1 == 'Д') and (s6 == 'Г' or s6 == 'Д')):
                            k += 1
print(k)
