# from itertools import combinations, product
# from bisect import bisect_left

# def solution(dices):
#     n = len(dices)
#     max_win, best = -1, []
    
#     for a_idx in combinations(range(n), n // 2):
#         b_idx = [i for i in range(n) if i not in a_idx]

#         A = [sum(dices[i][r] for i, r in zip(a_idx, rolls))
#              for rolls in product(range(6), repeat=n//2)]
#         B = [sum(dices[i][r] for i, r in zip(b_idx, rolls))
#              for rolls in product(range(6), repeat=n//2)]
#         B.sort()

#         wins = sum(bisect_left(B, a) for a in A)

#         if wins > max_win:
#             max_win, best = wins, a_idx

#     return [x + 1 for x in best]

from itertools import combinations, product
from bisect import bisect_left

def solution(dices):
    n = len(dices)
    max_win, best_comb = -1, []
    
    for a_comb in combinations(range(n), n // 2):
        b_comb = [i for i in range(n) if i not in a_comb]
        
        A = []
        for rolls in product(range(6), repeat = n // 2):
            tot = 0
            for i, r in zip(a_comb, rolls):
                tot += dices[i][r]
            A.append(tot)

        B = []
        for rolls in product(range(6), repeat = n//2):
            tot = 0
            for i, r in zip(b_comb, rolls):
                tot += dices[i][r]
            B.append(tot)

        B.sort()
        
        wins = 0
        for a in A:
            wins += bisect_left(B, a)

        if wins > max_win:
            max_win, best_comb = wins, a_comb

    return [i + 1 for i in best_comb]