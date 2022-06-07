from functools import lru_cache

def move(h):
    a,b = h
    return (a + 2, b), (a * 2, b), (a, b + 2), (a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h) >= 63:
        if sum(h) <= 74:
            return 'w'
        return 'l'
    
    if any(game(m) == 'w' for m in move(h)):
        return 'p1'
    if any(game(m) == 'p1' or game(m) == 'l' for m in move(h)):
        return 'b1'
    if any(game(m) == 'b1' for m in move(h)):
        return 'p2'
    if all(game(m) == 'p1' or game(m) == 'l' or game(m) == 'p2' for m in move(h)):
        return 'b2'
for s in range(1,48):
    print(s, game((15,s)))