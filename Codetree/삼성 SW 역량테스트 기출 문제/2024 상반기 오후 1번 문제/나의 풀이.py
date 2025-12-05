from collections import deque

def bfs(i, j, exits, grid):
    q = deque()
    q.append([i, j])
    v = [[0] * c for _ in range(r + 3)]
    v[i][j] = 1
    max_idx = 0
    
    # 이동 가능한 칸 (idx)
    li = [grid[i][j]]
    
    while q:
        si, sj = q.popleft()
        
        # BFS 돌면서 가장 남쪽의 칸으로 이동
        if max_idx < si:
            max_idx = si
            
        for dr in range(4):
            ni, nj = si + dx[dr], sj + dy[dr]
            if 0 <= ni < r + 3 and 0 <= nj < c and grid[ni][nj] in li and v[ni][nj] == 0:
                # 이때, 현재 골렘의 출구가 다른 골렘과 인접해 있다면 이동 가능
                # 출구이면 상하좌우 보면서 이동 가능한 칸 li에 집어넣기
                if (ni, nj) in exits:
                    for ddi, ddj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        nni, nnj = ni + ddi, nj + ddj
                        if 0 <= nni < r + 3 and 0 <= nnj < c and grid[nni][nnj] not in li and grid[nni][nnj] != 0 and v[nni][nnj] == 0:
                            li.append(grid[nni][nnj])
                    
                v[ni][nj] = 1
                q.append([ni, nj])
    
    return max_idx - 2
    

r, c, k = map(int, input().split())
golems = [list(map(int, input().split())) for _ in range(k)] # [출발 열 : c, 출구 d]
grid = [[0] * c for _ in range(r + 3)]
# 골렘 : 중앙 c, 출구 (d) (0: 북, 1: 동, 2: 남, 3: 서)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
cnt = 0
exits = set()
for idx, (j, d) in enumerate(golems):
    i = 1
    j -= 1
    di, dj = dx[d], dy[d]

    while True:
        move_flag = False
        bfs_flag = True
        # 남쪽으로 한칸 내려가기, 중심(i, j)기준 
            # i + 1이 r + 3보다 작고, (i + 1, j - 1), (i + 2, j), (i + 1, j + 1) 이 모두 비었다면
        if i < r + 1 and grid[i + 1][j - 1] == 0 and grid[i + 2][j] == 0 and grid[i + 1][j + 1] == 0:
            i += 1
            move_flag = True
        # 안되면 서쪽으로 회전, 중심 : (i, j), 출구: (d - 1) % 4
            # i + 1이 r + 3보다 작고, 
            # (i - 1, j - 1), (i, j - 2), (i + 1, j - 1)
            # (i + 1, j - 2), (i + 2, j - 1) 이 모두 비었다면
        elif i < r + 1 and 1 < j and grid[i - 1][j - 1] == 0 and grid[i][j - 2] == 0  and grid[i + 1][j - 1] == 0 and grid[i + 1][j - 2] == 0 and grid[i + 2][j - 1] == 0:
            i += 1
            j -= 1
            d = (d - 1) % 4
            move_flag = True
        # 안되면 동쪽으로 회전, 중심 : (i, j), 출구: (d + 1) % 4
            # (i - 1, j + 1), (i, j + 2), (i + 1, j + 1)
            # (i + 1, j + 2), (i + 2, j + 1) 이 모두 비었다면
        elif i < r + 1 and j < c - 2 and grid[i - 1][j + 1] == 0 and grid[i][j + 2] == 0  and grid[i + 1][j + 1] == 0 and grid[i + 1][j + 2] == 0 and grid[i + 2][j + 1] == 0:
            i += 1
            j += 1
            d = (d + 1) % 4
            move_flag = True

        # 더 못 움직인다면
        if not move_flag:
            # 골렘의 가장 위칸 중심(i, j) 기준 (i - 1, j)이 3보다 작다면 숲 초기화
            if i < 4:
                grid = [[0] * c for _ in range(r + 3)]
                exits = set()
                bfs_flag = False
                break
            else:
                exits.add((i + dx[d], j + dy[d]))
                grid[i][j] = grid[i - 1][j] = grid[i + 1][j] = grid[i][j - 1] = grid[i][j + 1] = idx + 1
                break
    
    # 정령의 최종 위치의 행(j) 번호의 합 구하기
    if bfs_flag:
        cnt += bfs(i, j, exits, grid)

print(cnt)