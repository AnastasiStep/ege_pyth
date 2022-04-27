from functools import lru_cache

def moves(h):
    return (h + 1),(h * 3)

@lru_cache(None)
def game(h):
    if h>=71:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m)=='P1' for m in moves(h)):
        return 'B1'
    if any(game(m)=='B1' for m in moves(h)):
        return 'P2'
    if all(game(m)=='P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'

for i in range(1, 67):
    if game(i) is not None:
        print(i, game(i))

# 3) 23 22 21