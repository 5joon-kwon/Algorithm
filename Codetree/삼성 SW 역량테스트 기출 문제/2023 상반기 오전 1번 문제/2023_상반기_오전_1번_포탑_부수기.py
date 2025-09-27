from collections import deque

import sys
sys.stdin = open('test.txt', 'r')

def search_portop(arr, flag):
    mlist = [] # 공격력, 턴, 행 + 열, 열, 행
    if flag == 1:
        mdam = 5001
    else:
        mdam = 0
        
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0:
                continue
            
            if flag == 1:
                if mdam > arr[i][j]:
                    mdam = arr[i][j]
                    mlist = [[arr[i][j], -turn[i][j], -(i + j), -j, i]] 
                elif mdam == arr[i][j]:
                    mlist.append([arr[i][j], -turn[i][j], -(i + j), -j, i])
            else:
                if mdam < arr[i][j]:
                    mdam = arr[i][j]
                    mlist = [[-arr[i][j], turn[i][j], (i + j), j, i]]
                elif mdam == arr[i][j]:
                    mlist.append([-arr[i][j], turn[i][j], (i + j), j, i])
    
    mlist.sort()
    return mlist[0]

def bfs(si, sj, ei, ej):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    
    q.append((si, sj))
    visited[si][sj] = (si, sj)
    
    while q:
        ci, cj = q.popleft()
        
        # laser 공격 가능
        if (ci, cj) == (ei, ej):
            arr[ci][cj] = max(0, arr[ci][cj] - arr[si][sj])
            
            while True:
                ci, cj = visited[ci][cj]
                
                if (ci, cj) == (si, sj):
                    return True
                
                arr[ci][cj] = max(0, arr[ci][cj] - arr[si][sj] // 2)
                fset.add((ci, cj))
        
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di) % N, (cj + dj) % M
            if visited[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)
    
    return False

def bomb(si, sj, ei, ej):
    arr[ei][ej] = max(0, arr[ei][ej] - arr[si][sj])
    for di, dj in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
        ni, nj = (ei + di) % N, (ej + dj) % M
        if arr[ni][nj] != 0 and (ni, nj) != (si, sj):
            arr[ni][nj] = max(0, arr[ni][nj] - arr[si][sj] // 2)
            fset.add((ni, nj))

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]

for T in range(1, K + 1):
    atdam, atT, ats, atj, ati = search_portop(arr, 1)
    ats, atj = -ats, -atj
    hdam, hT, hs, hj, hi = search_portop(arr, 0)
    
    arr[ati][atj] += N + M
    turn[ati][atj] = T
    
    fset = set()
    fset.add((ati, atj))
    fset.add((hi, hj))
    
    if not bfs(ati, atj, hi, hj):
        bomb(ati, atj, hi, hj)   
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and (i, j) not in fset:
                arr[i][j] += 1 
    
    cnt = N * M
    for a in arr:
        cnt -= a.count(0)
    if cnt <= 1:
        break
    
ans = 0
for i in range(N):
    for j in range(M):
        if ans < arr[i][j]:
            ans = arr[i][j]
            
print(ans)