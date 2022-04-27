#1
print('1-----------------------')
maxa = -1
c = 0
for i in range(1012, 6548):
    if i % 3 == 0 and i % 9 != 0 and i % 14 != 0 and i % 21 != 0 and i % 24 != 0:
        if i > maxa:
            maxa = i;
        c += 1
print(c, maxa);

#2
print('2-----------------------')
mina = 100000
c = 0
for i in range(2345, 98765):
    if (i % 7 == 0 and i % 6 != 0 and i % 3 != 0 and ((i % 10 + (i % 100) // 10) % 2 == 0)):
        if (i < mina):
            mina = i
        c += 1
print(c, mina)

#3
print('3-----------------------')
mina = 100000
c = 0
for i in range(1234, 6789):
    n = i
    b = ''
    while n > 0:
        b = str(n % 8) + b
        n = n // 8
    n = int(b)
    suma = 0
    mult = 1
    while n > 0:
        digit = n % 10
        suma = suma + digit
        mult = mult * digit
        n = n // 10
    if (suma == 12 and mult % 5 == 0):
        if (i < mina):
            mina = i
        c += 1
print(c, mina)

#4
print('4-----------------------')
mina = 1000000
c = 0
for i in range(1001, 10000):
    n = i
    b = ''
    while n > 0:
        b = str(n % 8) + b
        n = n // 8
    n = int(b)
    if (i % 10 == 5 and n % 10 == 1 and i % 27 == 0 and i % 12 != 0 and i % 14 != 0 and i % 18 != 0):
        if (i < mina):
            mina = i
        c += 1
print(c, mina)

#5
print('5-----------------------')
sum = 0
c = 0
for i in range(468, 2974):
    d = 0
    for j in range(1, i):
        if (j % 3 == 0 and i % j == 0):
            d += 1
    if (d <= 10):
        c += 1
        sum += i
print(c, sum)

#6
print('6-----------------------')
maxa = 0
mina = 300000
for i in range(200005, 200190):
    d = 0
    for j in range(1, i):
        if (j % 2 != 0 and i % j == 0):
            d += 1
    #print (d)
    if (d == 6):
        if (i  < mina):
            mina = i
        if (i > maxa):
            maxa = i
print(mina, maxa)

#7
print('7-----------------------')
for i in range(1050, 20800):
    d = 0
    for j in range(2, i - 1):
        if (i % j == 0):
            d += 1
    if (d == 3):
        print(i)
        for j in range(2, i - 1):
            if (i % j == 0):
                print(j, end = ' ')
        print()

#8
print('8-----------------------')
min = 100001
c = 0
for i in range(10000, 100000):
    n = i
    suma = 0
    while n > 0:
        digit = n % 10
        suma = suma + digit
        n = n // 10
    if (suma % 18 == 0):
        c += 1
        if (i < mina):
            mina = i
print(c, mina)

#9
print('9-----------------------')
d = 2 
for i in range(2, int(67743 / 2) + 1):
    if 67743 % i == 0:
        d += 1
for i in range(98320, 98410):
    n = 2 
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            n += 1
    if (n == d):
        print(i)

#10
print('10----------------------')
for numb in range(65456, 98789):
    suma = 0
    for i in range(numb - 1, 1, -1):
        is_simple = 0
        if (numb % i == 0):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    is_simple = is_simple + 1
                    suma += i
    if (suma % 17 == 0 and suma != 0):
        print (numb, suma)