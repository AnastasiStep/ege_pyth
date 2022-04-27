import re
#1
x=49**12-7**10+7**8-49
c=0
while x:
    if x % 7 == 6:
        c+=1
    x//=7
print(c)
#2
x=27**4-9**5+3**8-25
c=0
while x:
    if x % 3 == 2:
        c+=1
    x//=3
print(c)
#3
x=3*16**8-4**5+3
c=0
while x:
    if x % 4 == 3:
        c+=1
    x//=4
print(c)
#4
x=2*9**10-3**5+5
c=0
while x:
    if x % 3 == 2:
        c+=1
    x//=3
print(c)
#5
x=5*36**7+6**10-36
c=0
while x:
    if x % 6 == 5:
        c+=1
    x//=6
print(c)
#6
x=4*125**4-25**4+9
c=0
while x:
    if x % 5 == 4:
        c+=1
    x//=5
print(c)
#7
x=9**8+3**25-14
c=0
while x:
    c += x % 3
    x//=3
print(c)
#8
n=9**17+3**16-27
b = ''
while n > 0:
    b = str(n % 3) + b
    n = n // 3
print(max(b.count('0'), b.count('1'), b.count('2')))
#9
n=9**5+3**7-14
b = ''
while n > 0:
    b = str(n % 3) + b
    n = n // 3
print(min(b.count('0'), b.count('1'), b.count('2')))
#10
x = 2**51 + 2**40 + 2**35 + 2**17 - 2**5
print(len(set(hex(x))) - 1)
#11
n = 4**4 * 5**69 - 70
b = ''
while n > 0:
    b = str(n % 5) + b
    n = n // 5
print(b.count('0'), b.count('1'), b.count('2'), b.count('3'), b.count('4'))
