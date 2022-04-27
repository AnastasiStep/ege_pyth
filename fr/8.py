a = ['А', 'В', 'Т', 'О', 'Р']
k = 0
for s1 in a:
    for s2 in a:
        for s3 in a:
            for s4 in a:
                k+=1
                if (s1 == 'Т' and s2 == 'А' and s3 == 'Р' and s4 == 'А'):
                    break
print(k)