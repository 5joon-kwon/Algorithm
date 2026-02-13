import heapq

def dijkstra(graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cur_dist, u = heapq.heappop(pq)

        if cur_dist > dist[u]:
            continue

        for v, w in graph[u]:
            minn = w + cur_dist
            if minn < dist[v]:
                dist[v] = minn
                heapq.heappush(pq, (minn, v))
    
    max_dist = 0
    for i in range(1, n + 1):
        if max_dist < dist[i]:
            max_dist = dist[i]
    
    return max_dist
        

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    i, j, d = map(int, input().split())
    graph[j].append((i, d))

print(dijkstra(graph, n))