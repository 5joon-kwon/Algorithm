from collections import deque

def bfs(s, c1, c2, graph):
    queue = deque([s])
    visited = set([s])
    cnt = 0
    
    while queue:
        cur = queue.popleft()
        cnt += 1
        
        for nxt in graph[cur]:
            if (cur == c1 and nxt == c2) or (cur == c2 and nxt == c1):
                continue
        
            if nxt in visited:
                continue

            queue.append(nxt)
            visited.add(nxt)
    
    return cnt
    
    
def solution(n, wires):
    graph = [[] for _ in range(n + 1)]
    answer = n + 1
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        cnt = bfs(v1, v1, v2, graph)
        other = abs(cnt - (n - cnt))
        answer = min(answer, other)

    return answer