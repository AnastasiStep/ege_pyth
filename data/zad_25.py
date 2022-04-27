numb = 9000000
k = 0
maxa = 0

while (numb <= 10000000):
    k = 0
    for i in range(numb - 1, 1, -1):
        is_simple = 0
        if (numb % i == 0):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    is_simple = is_simple + 1
            if (is_simple == 0):
                k += 1
    if (k > maxa):
        maxa = k
    numb += 1

k = 0

while (numb <= 10000000):
    k = 0
    for i in range(numb - 1, 1, -1):
        is_simple = 0
        if (numb % i == 0):
            for j in range(i - 1, 1, -1):
                if (i % j == 0):
                    is_simple = is_simple + 1
            if (is_simple == 0):
                k += 1
    if (maxa == k):
        break
    numb += 1
print(numb, maxa)