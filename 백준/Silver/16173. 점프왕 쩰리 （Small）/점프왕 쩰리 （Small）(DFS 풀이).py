N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * N for _ in range(N)]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    # 이미 방문했거나, 0칸 이동이면
    if visit[x][y] == 1 or graph[x][y] == 0:
        return

    # 목적지에 도착했다면
    if graph[x][y] == -1:
        visit[x][y] = 1
        return
    
    visit[x][y] = 1

    # 현재 위치에서 이동한 위치로 재귀
    dfs(x + graph[x][y], y)
    dfs(x, y + graph[x][y])

dfs(0, 0)

if visit[N - 1][N - 1] == 1:
    print('HaruHaru')
else:
    print('Hing')
