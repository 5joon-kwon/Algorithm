import heapq

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    # start -> start 까지의 거리는 0
    pq = [(0, start)]

    while pq:
        # start -> u 까지의 가장 짧은 거리는 cur_dist
        cur_dist, u = heapq.heappop(pq)

        # start -> u 까지 새로운 거리 > start -> u 까지 기존 거리 이면 skip
        if cur_dist > dist[u]:
            continue
        
        # u의 이웃한 v들을 보며 더 짧은 경로가 있다면 갱신
        for v, w in graph[u]:
            # minn: (start -> u) + (u -> v)
            minn = cur_dist + w
            # start -> u -> v 가 start -> v 보다 짧다면 갱신
            if minn < dist[v]:
                dist[v] = minn
                heapq.heappush(pq, (minn, v))
    
    return dist

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
A, B = map(int, input().split())

# A에서 각 노드까지 최단 거리
distA = dijkstra(n, graph, A)
# B에서 각 노드까지 최단 거리
distB = dijkstra(n, graph, B)
# A -> B 최단 거리
target = distA[B]

x = A
path = [A]

while x != B:
    # 다음 노드
    next = None
    # 사전순으로 앞선 순서: v 노드 기준 정렬 (오름차순)
    for v, w in sorted(graph[x]):
        # (A -> x) + (x -> v) + (v -> B) == A -> B
        # 이러면 같은 거리지만 사전순으로 앞선 노드를 선택하게 됨
        if distA[x] + w + distB[v] == target:
            next = v
            break
    x = next
    path.append(x)

print(target)
print(*path)