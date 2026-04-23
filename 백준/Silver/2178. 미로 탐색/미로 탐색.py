import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = 1

while q:
    si, sj = q.popleft()

    if (si, sj) == (n - 1, m - 1):
        print(visited[si][sj])
        break

    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == '1' and visited[ni][nj] == 0:
            q.append((ni, nj))
            visited[ni][nj] = visited[si][sj] + 1
