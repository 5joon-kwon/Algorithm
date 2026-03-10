import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(i, j):
    return 0 <= i < n and 0 <= j < m

def melt(i, j):
    q = deque([(i, j)])
    v = [[0] * m for _ in range(n)]
    v[i][j] = 1

    melt_li = []

    while q:
        si, sj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            if in_range(ni, nj):
                if grid[ni][nj] == 0 and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = 1
                elif grid[ni][nj] == 1 and v[ni][nj] == 0:
                    melt_li.append((ni, nj))
                    v[ni][nj] = 1
    
    for mi, mj in melt_li:
        grid[mi][mj] = 0
    
    return

time = 0
last = 0

while True:
    remain = sum(g.count(1) for g in grid)

    if remain == 0:
        break

    last = remain
    melt(0, 0)
    time += 1

print(time)
print(last)