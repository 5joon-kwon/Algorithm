# 양방향 그래프
# 임의로 주어진 두 정점은 무조건 통과 (두 정점 기준으로 최단거리 구하기)
# 이동했던 정점, 간선 모두 다시 이동 가능

import sys, heapq
input = sys.stdin.readline

def dijkstra(start, graph):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

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
    
    return dist

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist1 = dijkstra(1, graph)
distv1 = dijkstra(v1, graph)
distv2 = dijkstra(v2, graph)

# 여기서 문제: 1 -> v1 -> v2 -> n 경로보다 1 -> v2 -> v1 -> n 경로가 더 짧을 수 있다는 점을 생각 못했음!
if dist1[v1] == float('inf') or distv1[v2] == float('inf') or distv2[n] == float('inf'):
    print(-1)
else:
    print(dist1[v1] + distv1[v2] + distv2[n])