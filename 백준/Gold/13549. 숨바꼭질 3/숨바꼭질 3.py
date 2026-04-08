from collections import deque

n, k = map(int, input().split())

Max = 100001
dist = [-1] * Max
q = deque()

dist[n] = 0
q.append(n)

while q:
    next = q.popleft()

    if next == k:
        print(dist[next])
        break

    nx = next * 2
    if 0 <= nx < Max and dist[nx] == -1:
        q.appendleft(nx)
        dist[nx] = dist[next]

    nx = next - 1
    if 0 <= nx < Max and dist[nx] == -1:
        q.append(nx)
        dist[nx] = dist[next] + 1
        
    nx = next + 1
    if 0 <= nx < Max and dist[nx] == -1:
        q.append(nx)
        dist[nx] = dist[next] + 1