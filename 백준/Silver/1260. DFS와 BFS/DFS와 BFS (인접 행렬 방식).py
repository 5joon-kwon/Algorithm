from collections import deque

N, M, V = map(int, input().split())

# 그래프 초기화 (인접 행렬 방식)
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

def dfs(graph, start, visited):
    visited[start] = 1
    print(start, end=' ')
    
    # 인접 행렬 방식에서는 모든 정점을 순회해야함 -> O(모든 정점의 수)
    for neighbor in range(1, N + 1):
        if graph[start][neighbor] == 1 and visited[neighbor] == 0:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        
        # 인접 행렬 방식에서는 모든 정점을 순회해야함
        for neighbor in range(1, N + 1):
            if graph[current][neighbor] == 1 and visited[neighbor] == 0:
                queue.append(neighbor)
                visited[neighbor] = 1

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)