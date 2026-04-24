from collections import deque

n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = []

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    cnt = 1

    while q:
        si, sj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == '1' and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
    
    return cnt

for i in range(n):
    for j in range(n):
        if grid[i][j] == '1' and visited[i][j] == 0:
            ans.append(bfs(i, j))

ans.sort()

print(len(ans))
for i in range(len(ans)):
    print(ans[i])