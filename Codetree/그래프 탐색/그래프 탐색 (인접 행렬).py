N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
visited[1] = 1

for i in range(M):
    x, y = map(int, input().split())
    graph[x][y], graph[y][x] = 1, 1

cnt = 0

def dfs(present):
    global cnt
    for curr_v in range(1, N + 1):
        if graph[present][curr_v] and not visited[curr_v]:
            cnt += 1
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)
print(cnt)
