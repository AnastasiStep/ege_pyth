for k1 in range(1,20):
    for k2 in range(1,20):
        for k3 in range(1,20):
            s = '0' + '1' * k1 + '2' * k2 + '3' * k3 + '0'
            while not('00' in s):
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
                print(2 + k1 + k2 + k3, k1, k2, k3)
                exit(0)