# 도로: 0, 비도로: 1
# 집 (Sr, Sc), 공원 (Er, Ec)
# 1. 메두사 집 -> 공원 도로따라 한 칸씩 (상하좌우 순서) 최단 경로 (이동한 칸에 전사 있으면 전사 사라짐)
# 2. 메두사 기준 3, 5, 7, N 만큼 시선 (전사를 가장 많이 볼 수 있는 방향 우선 -> 같은 명수면 상하좌우 순서로 시선)
# 한명의 전사 뒤의 모든 전사는 안보임 -> 시선 받은 전사는 한턴 쉬고 이동
# 전사 M명 (ri, ci)에서 메두사한테 최단 경로로 이동 (어디든 이동 가능)
# 3. 전사는 상하좌우 순서로 이동 (메두사 시야로는 이동 x) -> 이동하다 메두사 만나면 공격 후 사라짐
# 4. 한 칸 더 좌우상하 순서로 이동
# 메두사가 공원에 도착 전까지 매 턴: 모든 전사가 이동한 거리의 합, 돌이 된 전사의 수, 메두사 공격한 전사의 수
# 도착하면 0 출력

from collections import deque

# 메두사 이동 (경로 복원이 핵심 !)
def find_route(sr, sc, er, ec):
    queue = deque()
    visit = [[0] * N for _ in range(N)]

    queue.append(((sr, sc)))
    visit[sr][sc] = ((sr, sc)) # 시작 위치 저장

    while queue:
        i, j = queue.popleft()
        if (i, j) == (er, ec):
            route = []
            i, j = visit[i][j]
            while (i, j) != (sr, sc):
                route.append((i, j))
                i, j = visit[i][j]
            return route[::-1] # 역방향 안해주면 도착 -> 출발 순서로 return 됨
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상하좌우 순서
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and road[ni][nj] == 0:
                queue.append((ni, nj))
                visit[ni][nj] = ((i, j)) # 도착 지점에 이전 위치 저장
    
    return -1

# 시선 8방향 (상, 우상, 우, 우하, 하, 좌하, 좌, 좌상)
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def mark_line(dr_view, i, j, dr):
    while 0 <= i < N and 0 <= j < N:
        dr_view[i][j] = 2 # 시선이 안닿는 곳
        i += di[dr]
        j += dj[dr]

def mark_safe(diagonal_dr, dr, ddi, ddj, dr_view): # 전사의 대각선 위치 2로 표시하기 위한 수
    ni, nj = ddi + di[dr], ddj + dj[dr] # 전사 뒤로 2 표시
    mark_line(dr_view, ni, nj, dr)

    ni, nj = ddi + di[diagonal_dr], ddj + dj[diagonal_dr] # 전사 대각선으로 2 표시
    while 0 <= ni < N and 0 <= nj < N:
        mark_line(dr_view, ni, nj, dr) # 대각선 뒤로 2 표시
        ni, nj = ni + di[diagonal_dr], nj + dj[diagonal_dr]

# 메두사의 시선 (전사들 위치, 메두사 위치, 시선방향)
def sight(warrior_locate, mi, mj, dr):
    dr_view = [[0] * N for _ in range(N)]
    stone_cnt = 0

    # [1] dr 방향으로 전사 없으면 1, 전사 있으면 뒤는 2 처리
    ni, nj = mi + di[dr], mj + dj[dr]
    while 0 <= ni < N and 0 <= nj < N:
        dr_view[ni][nj] = 1
        if warrior_locate[ni][nj] > 0: # 시선의 위치에 전사가 존재한다면
            stone_cnt += warrior_locate[ni][nj] # 전사를 돌로 만들고
            ni, nj = ni + di[dr], nj + dj[dr]
            mark_line(dr_view, ni, nj, dr) # 돌이 된 전사 뒤는 가려지도록 직선 처리
            break
        ni, nj = ni + di[dr], nj + dj[dr]

    # [2] 대각 방향으로 전사 없으면 1, 전사 있으면 뒤는 2 처리
    for diagonal_dr in ((dr - 1) % 8, (dr + 1) % 8): # 상하좌우 각 경우에서 좌우대각선 방향을 살피기 위해 (%8 핵심)
        ddi, ddj = mi + di[diagonal_dr], mj + dj[diagonal_dr] # 시선 대각 처리
        while 0 <= ddi < N and 0 <= ddj <N:
            if dr_view[ddi][ddj] == 0 and warrior_locate[ddi][ddj] > 0: # 전사 만나면
                dr_view[ddi][ddj] = 1
                stone_cnt += warrior_locate[ddi][ddj]
                mark_safe(diagonal_dr, dr, ddi, ddj, dr_view) # 전사의 뒤 + 대각선 2로 표시
                break # 대각선의 처음에서 만나면 그 뒤와 대각선 뒤 모두 2 처리됨
        
            ni, nj = ddi, ddj # 대각선 첫 위치에 전사가 없다면
            while 0 <= ni < N and 0 <= nj < N:
                if dr_view[ni][nj] == 0: # 시선이 갈 수 있으면
                    dr_view[ni][nj] = 1
                    if warrior_locate[ni][nj] > 0: # 전사가 있으면
                        stone_cnt += warrior_locate[ni][nj]
                        mark_safe(diagonal_dr, dr, ni, nj, dr_view)
                        break
                else:
                    break
                
                ni, nj = ni + di[dr], nj + dj[dr] # dr 방향으로 한칸 가서 다시 검증 (make_line 쓰지 않는 이유 : 전사가 있는지 파악해야하므로)

            ddi, ddj = ddi + di[diagonal_dr], ddj + dj[diagonal_dr] # 대각으로 한칸 가서 다시 검증

    return stone_cnt, dr_view


first = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
second = [(0, -1), (0, 1), (-1, 0), (1, 0)] # 좌우상하

def warrior_move(view, mi, mj): # 메두사 시선과 위치에 따른 전사 얼음/이동/공격
    move, attack = 0, 0
    for order in (first, second):
        for idx in range(len(warriors) - 1, -1, -1):
            wi, wj = warriors[idx]
            if view[wi][wj] == 1: # 시선 받았으면 전사 얼음
                continue
            
            distance = abs(mi - wi) + abs(mj - wj) # 메두사와 전사 거리
            for di, dj in order:
                ni, nj = wi + di, wj + dj
                if 0 <= ni < N and 0 <= nj < N and view[ni][nj] != 1 and (abs(mi - ni) + abs(mj - nj)) < distance:
                    if (ni, nj) == (mi, mj):
                        attack += 1
                        warriors.pop(idx) # pop은 index로만 가능
                    else:
                        warriors[idx] = (ni, nj) # 이동한 전사 위치 반영
                    move += 1
                    break # 다음 전사 이동
    return move, attack


N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
w = list(map(int, input().split()))
warriors = []
for i in range(0, len(w), 2):
    warriors.append((w[i], w[i + 1]))
road = [list(map(int, input().split())) for _ in range(N)]

# [0] BFS로 메두사 최단경로: 도로따라 공원까지(여러 개면 상하좌우 순) 없으면 -1
m_route = find_route(sr, sc, er, ec)

if m_route == -1:
    print(-1)
else:
    for mi, mj in m_route: # 메두사가 이동한 칸마다 시선 처리(돌이 된 전사) + (전사 이동 + 공격) 출력

        # [1] 메두사의 이동: 지정된 최단거리로 한 칸 이동 (전사 마주치면 삭제)
        for i in range(len(warriors) - 1, -1, -1): # 리스트 요소 삭제는 뒤에서부터 순회: 인덱스 밀림 현상 방지 !
            if warriors[i] == (mi, mj):
                warriors.pop(i)

        # [2] 메두사의 시선: 상하좌우 네 방향 가장 많이 돌로 만들 수 있는 방향찾기     
        # => view[]에 표시해서 이동시 참조(메두사시선 == 1, 전사에 가려진 곳 == 2, 빈 땅==0)
        warrior_locate = [[0] * N for _ in range(N)] # warrior_locate: 지도에 전사수 표시
        for wi, wj in warriors:
            warrior_locate[wi][wj] += 1

        view = []
        max_stone = -1 # 0으로 초기화하면 안됨

        for dr in (0, 4, 6, 2): # 상하좌우 순서로 시선처리
            stone, dr_view = sight(warrior_locate, mi, mj, dr) # 전사들 위치, 메두사 위치, 시선방향
            if max_stone < stone:
                max_stone = stone
                view = dr_view # 시선도 바꿔줘야 후에 전사들 이동 가능
        
        move_cnt, attack_cnt = 0, 0
        # [3] 전사들의 이동(한 칸씩 두번): 메두사 있는 경우 공격
        move_cnt, attack_cnt = warrior_move(view, mi, mj)

        print(move_cnt, max_stone, attack_cnt)
    print(0)
