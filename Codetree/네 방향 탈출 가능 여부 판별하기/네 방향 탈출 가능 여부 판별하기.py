from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
queue = deque()

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True    

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return True

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited[x][y] = True
                queue.append((x, y))
    
    return False

visited[0][0] = True
queue.append((0, 0))

if bfs():
    print(1)
else:
    print(0)
