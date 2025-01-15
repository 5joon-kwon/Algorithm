from collections import deque

N, M, V = map(int, input().split())

# 그래프 초기화 (인접 리스트 방식)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    
    # 인접 리스트 방식에서는 연결된 정점만 순회함 -> O(연결된 간선 수)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        
        # 인접 리스트 방식에서는 연결된 정점만 순회함
        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

dfs(graph, V, visited_dfs)
print()
bfs(graph, V, visited_bfs)
