# 체스판 왼쪽 상단 (1,1) 빈칸, 함정, 벽(바깥도 벽)
# 기사 위치 (r, c)를 좌측 상단으로 h x w 크기 -> (r + h - 1, c + w), 체력 : k
# (1) 기사 상하좌우 한 칸 이동, 이동 위치에 다른 기사 있으면 그 기사도 함께 한 칸 밀림
# 마지막 기사 뒤에 벽이 있다면 처음 기사 못움직임
# (2) 밀려난 기사들은 밀려난 곳에서 w x h 안에 있는 함정의 수만큼 피해입음 (체력 깎임)
# 밀어낸 기사는 피해 x, 체력보다 많이 데미지 입으면 삭제 (사라진 기사는 명령 안듣는다)
# Q턴 동안 생존한 기사들이 받은 대미지의 합 (죽으면 대미지에서 삭제)

from collections import deque
def move_unit(num, dr):
    queue = deque() # 처리할 기사 목록
    unit_list = [] # 방문 기록용 (중복 금지) visit이랑 같은 결
    queue.append(num)
    unit_list.append(num)
    damage = [0] * (N + 1)

    while queue:
        cur = queue.popleft()
        si, sj, h, w, k = unit[cur]
        ni, nj = si + dx[dr], sj + dy[dr]
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                if grid[i][j] == 2:
                    return
                if grid[i][j] == 1:
                    damage[cur] += 1
        
        # 겹치는 기사있는 경우 큐에 추가(모든 유닛 체크)
        for idx in unit:
            if idx in unit_list: # 중복 이동 금지 (A가 B를 밀었을 때, B는 A,C 제외하고 밀어야함)
                continue
            
            ti, tj, th, tw, tk = unit[idx]
            if ni > ti + th - 1 or ni + h - 1 < ti or nj > tj + tw - 1 or nj + w - 1 < tj:
                continue
            else:
                queue.append(idx)
                unit_list.append(idx)
    
    damage[num] = 0 # 명령 받아 움직인 기사는 대미지 0

    # 움직인 기사들 실제 이동시키고, 데미지가 체력이상이면 삭제처리
    for idx in unit_list:    
        i, j, h, w, k = unit[idx]
        if k <= damage[idx]:
            unit.pop(idx)
        else:
            ni, nj = i + dx[dr], j + dy[dr]
            unit[idx] = [ni, nj, h, w, k - damage[idx]]


L, N, Q = map(int, input().split())
# 벽을 2로 처리 + 기사들 좌표 수정 안해도 됨
grid = [[2] * (L + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L + 2)]
knight = [list(map(int, input().split())) for _ in range(N)] # 위치: (r, c) 방패: h x w 체력: k
order = [list(map(int, input().split())) for _ in range(Q)] # i번 기사 d(상, 우, 하 , 좌)방향 한 칸 이동

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

unit = {}
init_life = [0] * (N + 1)
for i in range(1, N + 1):
    unit[i] = knight[i - 1]
    init_life[i] = knight[i - 1][4]

for num, dr in order:
    if num in unit:
        move_unit(num, dr)

answer = 0
for idx in unit:
    answer += init_life[idx] - unit[idx][4]
print(answer)
