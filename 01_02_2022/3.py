x = ''
for i in range(0,121):
    x += '563'

while ('56' in x) or ('3333' in x):
    x = x.replace('56', '3')
    x = x.replace('3333', '3')
print(x)