# 미로 NxN 을 M명이 참가 (r,c) 위치 미로 첫칸 (1,1)
# 빈칸 0, 벽(이동x, 1-9 내구도 -> 회전하면 -1 -> 내구도 0이면 빈 칸), 출구
# 모든 참가자 동시에 한 칸씩 출구와 가까운 쪽으로 (abs) 상하좌우 이동
# 상하 우선, 못움직이면 움직이지말고, 한 칸에 두명 이상 가능
# 모든 참가자 이동했으면, 미로 회전
# -> (한 명 이상의 참가자 + 출구) 포함한 가장 작은 정사각형 (i 우선 j 나중) 시계방향 90도 회전, 회전된 벽 내구도 -1
# K초 동안 모든 참가자 탈출하면 성공, 모든 참가자의 이동 거리 합 + 출구 좌표 출력

N, M, K = map(int, input().split())
maze = [list(map(int, input().split()))for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split()) # 입력 받아서 -1씩 해줄 때
    maze[i][j] -= 1
ei, ej = map(lambda x: int(x) - 1, input().split())
maze[ei][ej] = -11 # 참가자 수 최대 10명

def find_square(maze):
    # [1] 출구 모든 사람 간의 가장 짧은 가로 또는 세로 거리 구하기 => L
    min_L = N # 최대로 초기화
    for i in range(N):
        for j in range(N):
            if -11 < maze[i][j] < 0:
                min_L = min(min_L, max(abs(ei - i), abs(ej - j)))

    # [2] (0,0)부터 순회하면서 길이 L인 정사각형에 출구와 사람이 있는지 체크 => 리턴 L+1
    for i in range(N - min_L): # min_L x min_L 이 N을 순회하는 범위
        for j in range(N - min_L):
            if i <= ei <= i + min_L and j <= ej <= j + min_L: # 비상구가 정사각형 안에 위치
                for si in range(i, i + min_L + 1):
                    for sj in range(j, j + min_L + 1):
                        if -11 < maze[si][sj] < 0:
                            return i, j, min_L + 1 # 출구와 사람이 min_L 차이이면 정사각형은 min_L + 1 크기

def find_exit(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == -11:
                return i, j

move = 0
num = M # 사람이 -1 이므로 count하면 빼줘야함
for _ in range(K):
    # [1] 모든 참가자 (동시에)한 칸 이동(출구 최단거리 방향 상/하 우선)
    nmaze = [x[:] for x in maze] # 모든 사람이 동시에 이동하므로 깊은 복사 해야함
    for i in range(N):
        for j in range(N):
            if -11 < maze[i][j] < 0: # 사람이면 (사람 중첩되면 -10까지 가능)
                distance = abs(ei - i) + abs(ej - j) # 사람과 출구 사이 거리
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상하 우선
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] <= 0 and distance > (abs(ei - ni) + abs(ej - nj)):
                        move += maze[i][j] # 칸에 있는 사람 수 만큼 더하기 (이동거리)
                        nmaze[i][j] -= maze[i][j] # 이동 처리
                        if maze[ni][nj] == -11:
                            num += maze[i][j]
                        else:
                            nmaze[ni][nj] += maze[i][j] # 다음 칸으로 이동한 사람 추가
                        break # 다음 사람 이동해야하므로

    maze = nmaze # 이동처리 다 한 미로 받기
    if num == 0:  #사람이 없으면 모두 탈출한 것이므로 끝
        break

    # [2] 미로회전(출구와 한 명이상 참가자를 포함하는 가장 작은 정사각형)
    si, sj, L = find_square(maze)
    rmaze = [x[:] for x in maze]
    for i in range(L):
        for j in range(L):
            rmaze[si + i][sj + j] = maze[si + L - 1 - j][sj + i] # 90도 회전
            if rmaze[si + i][sj + j] > 0:
                rmaze[si + i][sj + j] -= 1

    maze = rmaze
    ei, ej = find_exit(maze)

print(-move)
print(ei + 1, ej + 1)
