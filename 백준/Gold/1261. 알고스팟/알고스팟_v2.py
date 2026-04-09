from collections import deque

m, n = map(int, input().split())
maze = [list(input()) for _ in range(n)]

si, sj = 0, 0

# 벽을 최소 몇 개 부수는지
wall = [[float('INF')] * m for _ in range(n)]
wall[si][sj] = 0

q = deque()
q.append([si, sj])

while q:
    i, j = q.popleft()

    for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < m:

            if maze[ni][nj] == '0' and wall[ni][nj] > wall[i][j]:
                q.appendleft([ni, nj])
                wall[ni][nj] = wall[i][j]

            if maze[ni][nj] == '1' and wall[ni][nj] > wall[i][j] + 1:
                q.append([ni, nj])
                wall[ni][nj] = wall[i][j] + 1

print(wall[n - 1][m - 1])
