# 유적지 5x5, 각 칸에 유물 1~7 존재
# 1. 회전 : 3x3 격자 시계 방향 회전(90,180,270) 가능
# 회전 목표 : (1) 유물 조각 최대 (2) 각도 작은 (3) 격자 중심 열 작은 (4) 격자 중심 행 작은
# 2. 획득 : 상하좌우로 인접한 같은 숫자 3개 이상 -> 유물 1개
# 3. 유물 재생성 : 벽면의 숫자 순서대로 작은 열, 큰 행 순서로 생성
# 4. 유물 재획득 
# --- 여기까지 1턴 --- 각 턴마다 유물의 가치 (조각) 총합 출력
# 획득 못하면 종료 

# 1. 중심좌표 (1, 1) 시작 
# (1) 90 (3) 180 (4) 270 -> 3번중 가장 큰 수 저장 (같으면 두고, 없으면 넘기기)

# 2. 가장 큰 유물 찾았으면 삭제하고 벽에 쓴 수 순서대로 채우기
# 벽의 숫자는 pop(0)
# 재생성된 유물 찾고 숫자 채우고 반복

# 3. 유물 없으면 1턴 끝 결과 출력 및 1-3 과정 반복

def rotate(ngrid, si, sj): # 격자 회전
    rot_grid = [x[:] for x in ngrid] # 깊은 복사
    for i in range(3):
        for j in range(3):
            rot_grid[si + i][sj + j] = ngrid[si + 3 - j - 1][sj + i] # 격자 회전 !
    return rot_grid

from collections import deque
def bfs(ngrid, visit, si, sj, clear):
    queue = deque()
    sset = set() # 유물 위치 저장 위해
    visit[si][sj] = 1
    cnt = 0
    queue.append((si, sj))
    sset.add((si, sj))
    cnt += 1

    while queue:
        i, j = queue.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and visit[ni][nj] == 0 and ngrid[ni][nj] == ngrid[i][j]:
                visit[ni][nj] = 1
                queue.append((ni, nj))
                sset.add((ni, nj))
                cnt += 1
        
    if cnt >= 3:
        if clear == 1:
            for i, j in sset:
                ngrid[i][j] = 0
        return cnt
    else:
        return 0

def count_and_clear(ngrid, clear): # 유물 개수 세기
    visit = [[0] * 5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if visit[i][j] == 0:
                cnt += bfs(ngrid, visit, i, j, clear)
    return cnt

K, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))
cnt_list = [] # K턴마다 저장할 유물의 개수

for _ in range(K): # 유물이 같을 때의 조건을 중첩 for문으로 자연으럽게 구현 !
    max_cnt = 0
    for rot in range(1, 4): # 회전수
        for j in range(3): # 열 우선 (중심좌표 1,2,3)
            for i in range(3): # 행 우선(중심좌표 1,2,3)
                ngrid = [x[:] for x in grid] # 원본 격자 깊은 복사
                for _ in range(rot): # 회전 1~3번
                    ngrid = rotate(ngrid, i, j) # 회전시킬 격자, 시작점

                cnt = count_and_clear(ngrid, 0)
                if max_cnt < cnt:
                    max_cnt = cnt
                    max_grid = ngrid # 최대 격자에서 유물 찾아야 하므로 저장
    if max_cnt == 0:
        break
    
    result = 0
    grid = max_grid # 유물이 최대일 때 격자
    while True:
        rec = count_and_clear(grid, 1)
        if rec == 0:
            break
        result += rec

        for j in range(5):
            for i in range(4, -1, -1): # 큰 행부터 작은 열 순서로 채우기
                if grid[i][j] == 0:
                    grid[i][j] = wall.pop(0)
    
    cnt_list.append(result)

print(*cnt_list)
        
