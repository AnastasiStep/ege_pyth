f = False
for a in range(70):
    for b in range(70):
        for c in range(70):
            s = '0' + '1'*a + '2'*b + '3'*c
            while(('01' in s) or ('02' in s) or ('03' in s)):
                s = s.replace('01', '2302')
                s = s.replace('02', '10')
                s = s.replace('03', '201')
            if s.count('1') == 58 and s.count('2') == 23 and s.count('3') == 15:
                print(a, b, c)
                f = True
                break
        if f: break
    if f: break