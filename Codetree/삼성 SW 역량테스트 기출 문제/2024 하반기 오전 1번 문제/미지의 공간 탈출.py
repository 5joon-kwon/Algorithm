# 시간 이상 현상 : (ri, ci)시작해서 vi의 배수 턴마다 di로 한 칸씩 확산 (빈 공간으로만 확산)
# 시간의 벽 위치 : space_map의 3 자리
# 탈출구 위치 : space_map의 4 자리
# 타임머신 위치 : time_map의 2 자리
# 0 : 이동 가능, 1 : 장애물
from collections import deque

def find_3d_start():
    for i in range(M):
        for j in range(M):
            if time_wall[4][i][j] == 2:
                return 4, i, j

def find_2d_end():
    for i in range(N):
        for j in range(N):
            if space_map[i][j] == 4:
                space_map[i][j] = 0
                return i, j

def find_2d_time_wall():
    for i in range(N):
        for j in range(N):
            if space_map[i][j] == 3:
                return i, j

def find_3d_end_2d_start(): # return 평면, time_wall 탈출 좌표, space_map 탈출 좌표
    si, sj = find_2d_time_wall()

    for i in range(si, si + M):
        for j in range(sj, sj + M):
            if space_map[i][j] != 3: # 현재 위치가 3이 아니라면
                continue

            if space_map[i][j + 1] == 0: # 우측
                return 0, M - 1, (M - 1) - (i - si), i, j + 1 # 전개도 좌표 변환 주의
            elif space_map[i][j - 1] == 0: # 좌측
                return 1, M - 1, i - si, i, j - 1
            elif space_map[i + 1][j] == 0: # 아래
                return 2, M - 1, j - sj, i + 1, j
            elif space_map[i - 1][j] == 0: # 위
                return 3, M - 1, (M - 1) - (j - sj), i - 1, j # # 전개도 좌표 변환 주의
    
    return -1

def bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d):
    queue = deque([(sk_3d, si_3d, sj_3d)])
    visit = [[[0] * M for _ in range(M)] for _ in range(5)] # 각 면에 대한 방문처리 + 이동 거리 알기 위함 [0]
    visit[sk_3d][si_3d][sj_3d] = 1

    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        k, i, j = queue.popleft()
        if (k, i, j) == (ek_3d, ei_3d, ej_3d): # 종료 조건
            return visit[k][i][j]
        
        for di, dj in move:
            ni, nj = i + di, j + dj

            if ni < 0: # 위쪽 방향으로 넘어갈 때
                if k == 4: # 윗면 -> 북
                    nk, ni, nj = 3, 0, (M - 1) - j
                elif k == 0: # 동 -> 윗면
                    nk, ni, nj = 4, (M - 1) - j, M - 1
                elif k == 1: # 서 -> 윗면
                    nk, ni, nj = 4, j, 0
                elif k == 2: # 남 -> 윗면
                    nk, ni, nj = 4, (M - 1), j
                elif k == 3: # 북 -> 윗면
                    nk, ni, nj = 4, 0, (M - 1) - j
            elif ni >= M: # 남쪽 방향으로 넘어갈 때
                if k == 4:
                    nk, ni, nj = 2, 0, j
                else:      # 이 조건 없으면 아래 if문으로 넘어가서 index 벗어남
                    continue
            elif nj < 0: # 왼쪽 방향으로 넘어갈 때
                if k == 4: # 윗면 -> 서
                    nk, ni, nj = 1, 0, i
                else:
                    nk, ni, nj = left[k], i ,M - 1
            elif nj >= M: # 오른쪽 방향으로 넘어갈 때
                if k == 4: # 윗면 -> 동
                    nk, ni, nj = 0, 0, (M - 1) - i
                else:
                    nk, ni, nj = right[k], i, 0
            else: # 한 면 내에서 이동
                nk = k
        
            if visit[nk][ni][nj] == 0 and time_wall[nk][ni][nj] == 0:
                queue.append((nk, ni, nj))
                visit[nk][ni][nj] = visit[k][i][j] + 1 # 이동 거리 표시
    
    return -1

def bfs_2d(distance_3d, time_change_map, si_2d, sj_2d, ei_2d, ej_2d):
    queue = deque([(si_2d, sj_2d)])
    time_change_map[si_2d][sj_2d] = distance_3d
    
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        i, j = queue.popleft()
        if (i, j) == (ei_2d, ej_2d):
            return time_change_map[i][j]

        for di, dj in move:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and space_map[ni][nj] == 0 and time_change_map[i][j] + 1 < time_change_map[ni][nj]:
                queue.append((ni, nj))
                time_change_map[ni][nj] = time_change_map[i][j] + 1
    return -1


N, M, F = map(int, input().split())
space_map = [list(map(int, input().split())) for _ in range(N)]
# 0:동, 1:서, 2:남, 3:북, 4:위
time_wall = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
time_change = [list(map(int, input().split())) for _ in range(F)]

sk_3d, si_3d, sj_3d = find_3d_start()
ei_2d, ej_2d = find_2d_end()
ek_3d, ei_3d, ej_3d, si_2d, sj_2d = find_3d_end_2d_start()

left = {0:2, 1:3, 2:1, 3:0} # bfs에서 면을 왼쪽으로 돌 때
right = {0:3, 1:2, 2:0, 3:1} # bfs에서 면을 오른쪽으로 돌 때
distance_3d = bfs_3d(sk_3d, si_3d, sj_3d, ek_3d, ei_3d, ej_3d) # 시간의 벽 이동거리
time_direction = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북 순서
final_distance = 0

if distance_3d != -1:
    time_change_map = [[401] * N for _ in range(N)] # 시간이상현상 처리
    for ri, ci, di, vi in time_change:
        time_change_map[ri][ci] = 1
        for m in range(1, N + 1):
            ti, tj = ri + time_direction[di][0] * m, ci + time_direction[di][1] * m # m 시간 만큼 di 방향 이동
            rt = vi * m # 해당 칸까지 도달하는 데 걸리는 시간 : 주기 * 시간
            if 0 <= ti < N and 0 <= tj < N and space_map[ti][tj] == 0 and (ti, tj) != (ei_2d, ej_2d):
                if time_change_map[ti][tj] > rt:
                    time_change_map[ti][tj] = rt
            else:
                break
    
    final_distance = bfs_2d(distance_3d, time_change_map, si_2d, sj_2d, ei_2d, ej_2d)

print(final_distance)