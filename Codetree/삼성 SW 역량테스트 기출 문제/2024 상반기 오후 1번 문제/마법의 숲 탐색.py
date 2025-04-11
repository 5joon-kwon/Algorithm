# 1~R 행 숲 (북쪽만 뚫려있음)
# 골렘 십자(5칸) - 정해진 칸으로 탈출
# i번째 골렘(탈출구 : di 방향)은 북쪽에서 중심이 ci 열에 위치하도록 이동

# 1. 남쪽으로 내려가다가 못가면 ?
# 2. -> 서쪽으로 한칸 이동 + 남쪽으로 이동 (출구 반시계로 90도 회전)
# 3. -> 동쪽으로 한칸 이동 + 남쪽으로 이동 (출구 시계로 90도 회전) 
# 4. 남쪽 끝 도달 -> 골렘 내에서 정령 이동 (골렘의 출구가 다른 골렘과 인접하면 다른 골렘으로 이동 가능)
# 5. 정령은 남쪽 끝으로 이동하고 종료 (각 정렬들의 최종 행(i) 위치를 누적합)
# if 골렘이 격자에서 벗어나 있으면 모든 골렘 out (이때 정령 위치는 포함 x), 다음 골렘부터 다시 숲 탐색

from collections import deque
def bfs(si, sj):
    queue = deque()
    visit = [[0] * (C + 2) for _ in range(R + 4)] # 감싼 숲의 방문 
    queue.append((si, sj))
    visit[si][sj] = 1
    max_i = 0 # 가장 남쪽에 위치

    while queue:
        i, j = queue.popleft()
        max_i = max(max_i, i) # 가장 아래 행 return
        for di, dj in ((-1 ,0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if visit[ni][nj] == 0 and (grid[ni][nj] == grid[i][j] or ((i, j) in exit_set and grid[ni][nj] > 1)):
                queue.append((ni, nj))
                visit[ni][nj] = 1
    
    return max_i - 2 # 골렘의 시작은 원래 숲보다 (-2, 0) 이므로

R, C, K = map(int, input().split())
grid = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)] # 골렘과 숲의 외곽을 다 감싸도록 설정
g_loc = [list(map(int, input().split())) for _ in range(K)] # 출발하는 열 cj, 출구 di 
ans = 0
num = 2 # 골렘 종류 표시
exit_set = set()

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for cj, di in g_loc:
    ci = 1 # 골렘의 중심 행

    while True:
        if grid[ci + 2][cj] == 0 and grid[ci + 1][cj - 1] == 0 and grid[ci + 1][cj + 1] == 0:
            ci += 1
        elif grid[ci - 1][cj - 1] == 0 and grid[ci][cj - 2] == 0 and grid[ci + 1][cj - 1] == 0 and grid[ci + 1][cj - 2] == 0 and grid[ci + 2][cj - 1] == 0:
            ci += 1
            cj -= 1
            di = (di - 1) % 4 # 반시계로 90도 회전
        elif grid[ci - 1][cj + 1] == 0 and grid[ci][cj + 2] == 0 and grid[ci + 1][cj + 1] == 0 and grid[ci + 1][cj + 2] == 0 and grid[ci + 2][cj + 1] == 0:
            ci += 1
            cj += 1
            di = (di + 1) % 4 # 시계로 90도 회전
        else:
            break
    
    if ci < 4: # 격자 밖에 위치
        grid = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)] # 숲 초기화
        exit_set = set() # 탈출구 좌표들 초기화
        num = 2
    else:
        grid[ci][cj] = grid[ci - 1][cj] = grid[ci + 1][cj] = grid[ci][cj - 1] = grid[ci][cj + 1] = num
        exit_set.add((ci + dx[di], cj + dy[di])) # 탈출구 좌표 저장
        num += 1
        ans += bfs(ci, cj)

print(ans)
