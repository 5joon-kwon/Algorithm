from collections import deque

n, k = map(int, input().split())

Max = 100001
dist = [float('INF')] * Max
q = deque()

dist[n] = 0
q.append(n)

while q:
    next = q.popleft()

    nx = next * 2
    if 0 <= nx < Max and dist[nx] > dist[next]:
        q.appendleft(nx)
        dist[nx] = dist[next]

    nx = next - 1
    if 0 <= nx < Max and dist[nx] > dist[next] + 1:
        q.append(nx)
        dist[nx] = dist[next] + 1
        
    nx = next + 1
    if 0 <= nx < Max and dist[nx] > dist[next] + 1:
        q.append(nx)
        dist[nx] = dist[next] + 1

print(dist[k])
