for k1 in range(1,100):
    for k2 in range(1,100):
        for k3 in range(1,100):
            s = '0' + '1' * k1 + '2' * k2 + '3' * k3 + '0'
            while not('01' in s or '02' in s or '03' in s):
                s = s.replace('01', '30', 1)
                s = s.replace('02', '3103', 1)
                s = s.replace('03', '1202', 1)
            if s.count('1') == 59 and s.count('2') == 40 and s.count('3') == 66:
                print(2 + k1 + k2 + k3, k1, k2, k3)
                exit(0)