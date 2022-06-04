'''19
def f(s,n):
    if s >= 29:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0:
            #Peti
            return f(s + 1, n + 1) and f(s*2, n + 1)
        else:
            #Vani
            return f(s + 1, n + 1) or f(s*2, n + 1)
for s in range(1,29):
    if f(s,0) == True:
        print(s)
'''

''' 20
def f(s,n):
    if s >= 29:
        if n == 3: return True
        else: return False
    else:
        if n >= 3: return False
        elif n % 2 != 0:
            #Vani
            return f(s + 1, n + 1) and f(s*2, n + 1)
        else:
            #Peti
            return f(s + 1, n + 1) or f(s*2, n + 1)
for s in range(1,29):
    if f(s,0) == True:
        print(s)
'''

def f(s,n): #perv or vtor
    if s >= 29:
        if (n == 2) or (n == 4): return True
        else: return False
    else:
        if n >= 4: return False
        elif n % 2 == 0:
            #Peti
            return f(s + 1, n + 1) and f(s*2, n + 1)
        else:
            #Vani
            return f(s + 1, n + 1) or f(s*2, n + 1)

def g(s,n): #tolko perv
    if s >= 29:
        if n == 2: return True
        else: return False
    else:
        if n >= 2: return False
        elif n % 2 == 0:
            #Peti
            return g(s + 1, n + 1) and g(s*2, n + 1)
        else:
            #Vani
            return g(s + 1, n + 1) or g(s*2, n + 1)

for s in range(1,29):
    if f(s,0) == True and g(s,0) == False:
        print(s)