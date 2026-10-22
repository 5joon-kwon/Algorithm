from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    si, sj, ei, ej = 0, 0, 0, 0
    
    # . 빈 공간, R 로봇 위치, D 장애물, G 목표
    f1, f2, f3 = False, False, False
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                si, sj = i, j
                f1 = True
            elif board[i][j] == 'G':
                ei, ej = i, j
                f2 = True
            else:
                continue
        
            if f1 and f2:
                f3 = True
                break
        if f3:
            break
    
    queue = deque([[0, si, sj]])
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1
    
    while queue:
        cnt, i, j = queue.popleft()
        
        if (i, j) == (ei, ej):
            return cnt
        
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i, j
            
            while True:
                ti, tj = ni + di, nj + dj
                
                if not (0 <= ti < n and 0 <= tj < m):
                    break
                
                if  board[ti][tj] == 'D':
                    break
            
                ni, nj = ti, tj
            
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                queue.append((cnt + 1, ni, nj))
                
    return -1