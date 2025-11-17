from collections import deque

def bfs(i, j, visited):
    q = deque([[i, j]])
    visited[i][j] = 0
    
    while q:
        si, sj = q.popleft()
        
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = si + di, sj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N:
                continue
            
            if visited[ni][nj] == 0:
                continue
            
            q.append([ni, nj])
            visited[ni][nj] = 0
    
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_rain = 0
res = 1

for i in grid:
    max_rain = max(i)

for i in range(max_rain):
    for j in range(N):
        for k in range(N):
            if grid[j][k] > 0:
                grid[j][k] -= 1
    
    cnt = 0
    visited = [row[:] for row in grid]           
    for l in range(N):
        for r in range(N):
            if visited[l][r] != 0:
                cnt += 1
                bfs(l, r, visited)
                res = max(res, cnt)    
    
print(res)