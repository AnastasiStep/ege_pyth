f = open('python/kim-241_test.txt')
s = f.readline()

count = count_max = 1
for i in range(len(s)-1):
    if (s[i] == s[i+1]) and (s[i] != 'Z'):
        count += 1
    else:
        if count_max < count:
            count_max = count
        count = 1
if count_max < count:
    count_max = count
 
print(count_max)