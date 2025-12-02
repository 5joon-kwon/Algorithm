import sys
sys.stdin = open('test.txt', 'r')

from collections import deque

k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
npieces = list(map(int, input().split()))

# 격자 돌리기
def rotate(si, sj, n):
    ngrid = [row[:] for row in grid]

    if n == 0:
        for i in range(3):
            for j in range(3):
                ngrid[si + (i - 1)][sj + (j - 1)] = grid[si + (1 - j)][sj + (i - 1)]
    elif n == 1:
        for i in range(3):
            for j in range(3):
                ngrid[si + (i - 1)][sj + (j - 1)] = grid[si + (1 - i)][sj + (1 - j)]
    else:
        for i in range(3):
            for j in range(3):
                ngrid[si + (i - 1)][sj + (j - 1)] = grid[si + (j - 1)][sj + (1 - i)]
    
    return ngrid

# 유물 찾기
def bfs(si, sj, visited, graph, plist):
    q = deque()
    visited[si][sj] = 1
    q.append([si, sj])
    li = [[si, sj]]
    
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and graph[ni][nj] == graph[si][sj] and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append([ni, nj])
                li.append([ni, nj])

    if len(li) >= 3:
        plist.extend(li)

# 조각 위치 (열 작은, 행 큰 순서)
# k 턴
for _ in range(k):
    cnt = 0
    cnt_max, mpieces, mgrid = 0, [], []
    # 90, 180, 270 회전
    for r in range(3):
        for ri in range(1, 4):
            for rj in range(1, 4):
                new_grid = rotate(ri, rj, r)
                
                # 유물 탐색
                pieces = []
                v = [[0] * 5 for _ in range(5)]   
                for i in range(5):
                    for j in range(5):
                        if v[i][j] == 0:
                            bfs(i, j, v, new_grid, pieces)
                            
                # 유물 1차 획득을 최대화 (각도가 작은, 열 작은, 행 작은 순서)
                if cnt_max < len(pieces):
                    cnt_max, mpieces, mgrid = len(pieces), pieces, new_grid
                

    # 유물 없으면
    if cnt_max == 0:
        break
    
    # 유물 조각 개수 추가
    cnt += cnt_max

    # 유물 제거
    for i, j in mpieces:
        mgrid[i][j] = 0

    # 작은 열, 큰 행 순서로 조각 넣기
    mli = sorted(mpieces, key=lambda x: (x[1], -x[0]))    
    for i, j in mli:
        mgrid[i][j] = npieces.pop(0)

    # 2차 탐사
    if len(npieces) == 0:
        break
    
    while True:        
        second_piecies = []
        vsecond = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if vsecond[i][j] == 0:
                    bfs(i, j, vsecond, mgrid, second_piecies)

        # 유물 없으면 그만 찾기
        if len(second_piecies) == 0:
            break
        
        cnt += len(second_piecies)
        
        # 유물 제거
        for i, j in second_piecies:
            mgrid[i][j] = 0

        # 작은 열, 큰 행 순서로 조각 넣기
        sli = sorted(second_piecies, key=lambda x: (x[1], -x[0]))    
        for i, j in sli:
            mgrid[i][j] = npieces.pop(0)
    
    grid = mgrid
    print(cnt, end=' ')