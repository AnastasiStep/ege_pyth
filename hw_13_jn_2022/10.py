k = 0
for i in range(166006, 167000, 10):
    if (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0):
        k += 1
        print(i)
for i in range(1660006, 1670000, 10):
    if (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0):
        k += 1
        print(i)
    if k == 7:
        break