N = int(input())
grid = [list(input()) for _ in range(N)]

coins = []
si, sj, ei, ej = 0, 0, 0, 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            continue

        if grid[i][j] == 'S':
            si, sj = i, j
        elif grid[i][j] == 'E':
            ei, ej = i, j
        else:
            coins.append([grid[i][j], i, j])

coins.sort()
ans = float('inf')
comb = []

def dist():
    global ans
    d = 0

    for l in range(2):
        _, i, j = comb[l]
        _, ni, nj = comb[l + 1]
        d += abs(i - ni) + abs(j - nj)
    
    d += abs(si - comb[0][1]) + abs(sj - comb[0][2]) + abs(ei - comb[-1][1]) + abs(ej - comb[-1][2])
    ans = min(ans, d)

def combi(idx, cnt):
    if cnt == 3:
        dist()
        return
    
    for i in range(idx, len(coins)):
        comb.append(coins[i])
        combi(i + 1, cnt + 1)
        comb.pop()

combi(0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)