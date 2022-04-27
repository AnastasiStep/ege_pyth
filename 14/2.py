#1
x = 6**203 + 5*6**405 - 3*6**144 +77
c=0
while x:
    if x % 6 == 5:
        c+=1
    x//=6
print(c)
#2
n = 5*216**1256 - 5*36**1146 + 4*6**1053 - 1087
b = 0
while n > 0:
    b = b + n % 6
    n = n // 6
print(b)
#3
n = 16**44 * 16**30 - (32**5 * (8**40 - 8**12)*(16**17-32**4))
b = hex(n).replace('e', '1')
print(b)
#4
x = (5**300*15**100)-(25**50 + 125**100)
c=0
while x:
    if x % 5 != 4:
        c+=x % 5
    x//=5
print(c)
#5
maxi = 0
for n in range(0,1000):
    x = 7**500 + 7**200 - 7**50 - n
    c = 0
    while x:
        c+=x%7
        x//=7
    if maxi < c:
        maxi = c
print(maxi)
#6
x = 6*343**1156 - 5*49**1147 + 4*7**1153 - 875
c = 0
while x:
    c+=x%7
    x//=7
print(c)
#7
for x in range(0,1000):
    n = 64**12 - 8**14 + x
    b = ''
    while n > 0:
        b = str(n % 8) + b
        n = n // 8
    if b.count('7') == 12 and b.count('1') == 1:
        print(x)