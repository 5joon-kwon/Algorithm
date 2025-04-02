from collections import deque

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
answer = [[0] * N for _ in range(N)]
queue = deque()

for _ in range(K):
    s, e = map(int, input().split())
    queue.append((s - 1, e - 1))
    # 시작점 방문처리 (킥 포인트)
    visited[s - 1][e - 1] = True
    answer[s - 1][e - 1] = 1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 1:
        return False
    return True

def bfs():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    
    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                answer[new_x][new_y] = 1
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))

bfs()
print(sum(point for row in answer for point in row))