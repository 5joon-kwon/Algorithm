from collections import deque
import sys

sys.stdin = open('test.txt', 'r')

def rotate(narr, si, sj):
    rarr = [x[:] for x in narr]
    for i in range(3):
        for j in range(3):
            rarr[si + i][sj + j] = narr[si + 2 - j][sj + i]
    
    return rarr

def in_range(i, j):
    if 0 <= i < 5 and 0 <= j < 5:
        return True
    return False

def bfs(arr, visited, i, j, clear):
    q = deque()
    vset = set()
    q.append((i, j))
    visited[i][j] = 1
    vset.add((i, j))
    cnt = 1  
    
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj +dj
            if in_range(ni, nj) and arr[ci][cj] == arr[ni][nj] and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                vset.add((ni, nj))
                cnt += 1
    
    if cnt >= 3:
        if clear:
            for si, sj in vset:
                arr[si][sj] = 0
        return cnt
    else:
        return 0

def count_clear(arr, clear):
    visited = [[0] * 5 for _ in range(5)]
    cnt = 0
    
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                cnt += bfs(arr, visited, i, j, clear)
    
    return cnt
    

K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
piece = list(map(int, input().split()))
ans = []

for _ in range(K):
    max_cnt = 0
    for rot in range(1, 4):
        for j in range(3):
            for i in range(3):
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, i, j)
                
                tcnt = count_clear(narr, 0)
                if max_cnt < tcnt:
                    max_cnt = tcnt
                    marr = narr
                    
    if max_cnt == 0:
        break
   
    cnt = 0
    arr = marr
    while True:
        tcnt = count_clear(arr, 1)
        
        if tcnt == 0:
            break
        
        cnt += tcnt
        
        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = piece.pop(0)
    
    ans.append(cnt)
    
print(*ans)