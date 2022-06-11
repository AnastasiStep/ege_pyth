def f(s1, s2, n):
    if (s1 + s2) >= 63 and (s1 + s2) <= 74:
        if n == 2: return True
        else: return False
    elif s1 + s2 > 74:
        if n == 1: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0: 
            return f(s1 )