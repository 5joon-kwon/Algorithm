from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = 0
    
    queue = deque()
    visited = [[0] * m for _ in range(n)]
    queue.append([0, 0])
    visited[0][0] = 1
    
    while queue:
        si, sj = queue.popleft()
        
        if (si, sj) == (n - 1, m - 1):
            answer = visited[si][sj]
            break
        
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[si][sj] + 1
                
    if answer == 0:
        return -1
    return answer