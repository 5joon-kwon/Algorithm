N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 그리드 안에서는 인접 행렬 or 인접 리스트 사용하지 않아도 된다 !
visited = [[False] * M for _ in range(N)]
answer = [[0] * M for _ in range(N)]
order = 1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global order
    # 마지막에 도착하게 된다면
    if x == (N - 1) and y == (M - 1):
        return True

    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy 
    
        if can_go(new_x, new_y):
            answer[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = True
            # 재귀하다가 마지막에 도착하게 된다면 return
            if dfs(new_x, new_y):
                return True
    return False

if dfs(0, 0):
    print(1)
else:
    print(0)