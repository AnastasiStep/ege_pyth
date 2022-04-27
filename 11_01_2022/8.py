a = ['И', 'В', 'А', 'Н']
k = 0
for s1 in a:
    for s2 in a:
        for s3 in a:
            for s4 in a:
                for s5 in a:
                    s = s1 + s2 + s3 + s4 + s5
                    if (s.count('И') != 0):
                        k += 1
print(k)
