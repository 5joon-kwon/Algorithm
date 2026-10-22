from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    visited = [[0] * m for _ in range(n)]
    
    def bfs(num, i, j):
        queue = deque()
        queue.append([i, j])
        visited[i][j] = num
        size = 0
        
        while queue:
            si, sj = queue.popleft()
            size += 1
            
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = si + di, sj + dj
                
                if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1 and visited[ni][nj] == 0:
                    queue.append([ni, nj])
                    visited[ni][nj] = num
        
        return size

    # 0: 빈 땅, 1: 석유
    dic = {}
    num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                size = bfs(num, i, j)
                dic[num] = size
                num += 1
    
    for i in range(m):
        li = []
        for j in range(n):
            if land[j][i] != 0 and visited[j][i] not in li:
                li.append(visited[j][i])
        
        tsize = 0
        for k in li:
            tsize += dic[k]
        
        answer = max(answer, tsize)                
    
    return answer