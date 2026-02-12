import heapq

def dijkstra(graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    # PriorityQueue : (거리, 정점)
    pq = [(0, start)]
    
    while pq:
        # heapq: 리스트의 첫 번째 원소를 기준으로 최소 튜플을 반환
        cur_dist, u = heapq.heappop(pq)
        
        # lazy deletion: 더 짧은 거리로 온 적 있다면 skip
        if cur_dist > dist[u]:
            continue
        
        for v, w in graph[u]:
            minn = cur_dist + w
            if minn < dist[v]:
                dist[v] = minn
                heapq.heappush(pq, (minn, v))
    
    for i in range(2, n + 1):
        if dist[i] == float('inf'):
            print(-1)
        else:
            print(dist[i])  

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

dijkstra(graph, 1)
