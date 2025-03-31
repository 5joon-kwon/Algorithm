N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

order = 1
visited = [[False] * (N + 1) for _ in range(N + 1)]
answer = [[0] * (N + 1) for _ in range(N + 1)]

def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global order

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y):
            answer[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

dfs(0, 0)
print(answer)
