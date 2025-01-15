from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')
    
    for neighbor in range(1, N + 1):
        if graph[start][neighbor] == 1 and visited[neighbor] == 0:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        
        for neighbor in range(1, N + 1):
            if graph[current][neighbor] == 1 and visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = 1

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)