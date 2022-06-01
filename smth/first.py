def forr(n):
    summ = 0
    for i in n:
        summ += i
    return summ

def whilee(n):
    summ = 0
    i = 0
    while i < len(n):
        summ += n[i]
        i += 1
    return summ

def rec(n, i, summ):
    if i < len(n):
        return rec(n, i + 1, summ + n[i])
    else:
        return summ

print(forr([1,1,1]))
print(whilee([1,1,1]))
print(rec([1,1,1],0,0))