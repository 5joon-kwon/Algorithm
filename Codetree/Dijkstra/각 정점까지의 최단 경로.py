import heapq

def dijkstra(graph, start):
    dist = [float('inf')] * (n + 1)
    dist[k] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)

        if cur_dist > dist[u]:
            continue
        
        for v, w in graph[u]:
            minn = cur_dist + w
            if minn < dist[v]:
                dist[v] = minn
                heapq.heappush(pq, (minn, v))
    
    for i in range(1, n + 1):      
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])


n, m = map(int, input().split())
k = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    # 양방향 그래프
    graph[u].append([v, w])
    graph[v].append([u, w])

dijkstra(graph, k)