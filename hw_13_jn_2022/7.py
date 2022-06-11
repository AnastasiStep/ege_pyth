import re


def f(s1 , s2, n):
    if s1 + s2 > 80:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0: return 