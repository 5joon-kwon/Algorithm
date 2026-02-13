import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    # v 정점으로 오기 전 정점 저장
    path = [-1] * (n + 1)

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
                # v로 오기 전 정점 u 저장
                path[v] = u
    
    return dist, path

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
A, B = map(int, input().split())

dist, path = dijkstra(n, graph, A)
print(dist[B])

# B -> A 로 역추적
route = []
p = B

while p != -1:
    route.append(p)
    if p == A:
        break
    
    # 하나 전으로 이동
    p = path[p]

route.reverse()
print(*route)
