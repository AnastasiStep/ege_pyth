x=6**54+216**21-12
c=0
while x:
    if x % 6 == 5:
        c+=1
    x//=6
print(c)