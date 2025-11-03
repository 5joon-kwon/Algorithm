from collections import deque

def bfs(si, sj, grid):
    q = deque([(si, sj)])
    grid[si][sj] = 1
    a = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx >= M or nx < 0 or ny >= N or ny < 0:
                continue

            if grid[nx][ny] == 0:
                q.append([nx, ny])
                grid[nx][ny] = 1
                a += 1
    
    return a

M, N, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    ly = M - ly - 1
    rx -= 1
    ry = M - ry

    for i in range(ry, ly + 1):
        for j in range(lx, rx + 1):
            grid[i][j] = 1

cnt = 0
area = []
visited = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            cnt += 1
            area.append(bfs(i, j, grid))

area.sort()
print(cnt)
for i in area:
    print(i, end = ' ')