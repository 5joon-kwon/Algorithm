N = int(input())
M = int(input())
count = 0

def dfs(start):
    global count
    visit[start] = 1
    
    for i in range(N + 1):
        if graph[start][i] == 1 and visit[i] != 1:
            dfs(i)
            count += 1

graph = [[0] * (N + 1) for _ in range(N + 1)]
visit = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(1)
print(count)
