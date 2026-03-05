import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline
import heapq

INF = float('inf')
def dijkstra(start, graph):
    dist = [[INF] * m for _ in range(n)]
    dist[start[0]][start[1]] = 0

    pq = [(0, start)]

    while pq:
        cur_w, u = heapq.heappop(pq)

        if cur_w > dist[u[0]][u[1]]:
            continue
        
        if u[0] + 1 == n and u[1] + 1 == m:
            return cur_w
        
        # graph[u] 대신, 여기서 이웃(v, w) 생성
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = u[0] + di, u[1] + dj
            
            if 0 <= ni < n and 0 <= nj < m:
                # 벽 (부숴야 이동 가능)
                if graph[ni][nj] == '1':
                    w = 1
                # 빈 방
                else:
                    w = 0
                minn = cur_w + w

                if minn < dist[ni][nj]:
                    dist[ni][nj] = minn
                    heapq.heappush(pq, (minn, (ni, nj)))
    
    return dist[n - 1][m - 1]

m, n = map(int, input().split())
maze = [list(input()) for _ in range(n)]

print(dijkstra((0, 0), maze))