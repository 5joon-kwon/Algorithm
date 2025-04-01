from collections import deque
queue = deque()

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = [[0] * M for _ in range(N)]
order = 1

def push(x, y):
    global order

    answer[x][y] = order
    order += 1
    visited[x][y] = True
    queue.append((x, y))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def bfs():
    dxs = [1, 0]
    dys = [0, 1]

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                push(new_x, new_y)

push(0, 0)
bfs()
print(answer)
