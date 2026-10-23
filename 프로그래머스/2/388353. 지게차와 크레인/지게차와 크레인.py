from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    grid = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            grid[i + 1][j + 1] = storage[i][j]
    
    for order in requests:
        if len(order) == 1:
            queue = deque()
            queue.append([0, 0])
            visited = [[0] * (m + 2) for _ in range(n + 2)]
            visited[0][0] = 1
            
            remove = set()
            
            while queue:
                si, sj  = queue.popleft()
                
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = si + di, sj + dj
                    if 0 <= ni < n + 2 and 0 <= nj < m + 2 and visited[ni][nj] == 0:
                        if grid[ni][nj] == 0:
                            queue.append([ni, nj])
                            visited[ni][nj] = 1
                        elif grid[ni][nj] == order:
                            remove.add((ni, nj))
            
            for i, j in remove:
                grid[i][j] = 0
        
        else:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if grid[i][j] == order[0]:
                        grid[i][j] = 0
        
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] != 0:
                answer += 1
    
    return answer