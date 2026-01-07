n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

bomb_loc = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_loc.append([i, j])

bombs = [
    [(-1, 0), (-2, 0), (0, 0), (1, 0), (2, 0)],
    [(-1, 0), (1, 0), (0, 0), (0, -1), (0, 1)],
    [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)]
]

ans = 0
v = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def explode(bi, bj, kind):
    cnt = 0
    changed_cor = []

    for i, j in bombs[kind]:
        ni, nj = bi + i, bj + j

        if not in_range(ni, nj):
            continue
        
        if v[ni][nj] == 0:
            cnt += 1

        v[ni][nj] += 1
        changed_cor.append([ni, nj])
    
    return cnt, changed_cor

def recover(cord):
    for i, j in cord:
        v[i][j] -= 1

def dfs(idx, cur_cnt):
    global ans

    if idx == len(bomb_loc):
        ans = max(ans, cur_cnt)
        return
    
    bi, bj = bomb_loc[idx]
    for kind in range(3):
        count, ccord = explode(bi, bj, kind)
        dfs(idx + 1, cur_cnt + count)
        recover(ccord)

dfs(0, 0)
print(ans)