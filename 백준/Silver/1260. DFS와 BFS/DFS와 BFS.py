from collections import deque

n, m, v = map(int, input().split())
grid = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    grid[x].append(y)
    grid[y].append(x)

for i in range(1, n + 1):
    grid[i].sort()

def bfs(v):
    q = deque([v])
    visit_bfs[v] = True

    while q:
        nv = q.popleft()
        print(nv, end=' ')
        
        for next in grid[nv]:
            if not visit_bfs[next]:
                q.append(next)
                visit_bfs[next] = True

def dfs(v):
    visit_dfs[v] = True
    print(v, end=' ')

    for next in grid[v]:
        if not visit_dfs[next]:
            dfs(next)

visit_dfs = [False] * (n + 1)
visit_bfs = [False] * (n + 1)

dfs(v)
print()
bfs(v)