from functools import lru_cache

def moves(h):
    a, b = h
    return (a + 2, b),(a, b + 2),(a + 3, b),(a, b + 3),(a * 2, b),(a, b * 2)

@lru_cache(None)
def game(h):
    if sum(h)>=78:
        return 'W'
    if any(game(m) == 'W' for m in moves(h)):
        return 'P1'
    if all(game(m)=='P1' for m in moves(h)):
        return 'B1'
    if any(game(m)=='B1' for m in moves(h)):
        return 'P2'
    if all(game(m)=='P1' or game(m) == 'P2' for m in moves(h)):
        return 'B2'

for i in range(1, 72):
    if game((11, i)) is not None:
        print(i, game((11,i)))

# 1) 7 1819 20
# 2) 17 67 2933
