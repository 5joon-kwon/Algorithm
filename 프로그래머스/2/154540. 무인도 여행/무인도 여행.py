from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = []
    visited = [[0] * m for _ in range(n)]
    
    def bfs(si, sj):
        queue = deque()
        queue.append([si, sj])
        visited[si][sj] = 1
        size = 0
        
        while queue:
            i, j = queue.popleft()
            size += int(maps[i] [j])
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] != 'X' and visited[ni][nj] == 0:
                    queue.append([ni, nj])
                    visited[ni][nj] = 1
        return size
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                answer.append(bfs(i, j))
    
    answer.sort()
    
    if len(answer) == 0:
        return [-1]
    
    return answer