from itertools import permutations 
words = set([''.join(w) for w in permutations("ОДЕКОЛОН")]) 
print(len(words))
words = [w for w in words if "ОО" not in w] 
print(len(words))