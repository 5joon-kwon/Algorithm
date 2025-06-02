import sys
from collections import deque
sys.stdin = open('./testcase.txt', 'r')

N, T = map(int, input().split())
F = [list(input()) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

def morning(B):
    for i in range(N):
        for j in range(N):
            B[i][j] += 1
    return

def find_group(F):
    visited = [[0] * N for _ in range(N)]
    group_id = 0
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                group_id += 1
                bfs(i, j, visited, group_id)
    
    return visited, group_id
                
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상, 하, 좌, 우

def bfs(si, sj, visited, group_id):
    queue = deque()
    queue.append((si, sj))
    visited[si][sj] = group_id
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and F[nx][ny] == F[x][y]:
                queue.append((nx, ny))
                visited[nx][ny] = group_id

def sorting(leader):
    one = []
    two = []
    three = []
    for i in range(len(leader)):
        if len(leader[i][2]) == 1:
            one.append(leader[i])
        elif len(leader[i][2]) == 2:
            two.append(leader[i])
        else:
            three.append(leader[i])
    
    one_sorted = sorted(one, key=lambda x: (-x[3], x[0], x[1])) # 신앙심 높은, 행 작은, 열 작은 순서
    two_sorted = sorted(two, key=lambda x: (-x[3], x[0], x[1]))
    three_sorted = sorted(three, key=lambda x: (-x[3], x[0], x[1]))
    
    return one_sorted + two_sorted + three_sorted

for _ in range(T):
    # 아침
    morning(B)

    # print('아침')
    # for i in B:
    #     print(i)
    # print()

    # 점심
    # 음식 같은 그룹 만들기
    group, group_cnt = find_group(F)

    # 그룹 리더 뽑기
    leader = []
    leader_coord = []
    for c in range(1, group_cnt + 1):
        max_B, max_i, max_j = 0, 0, 0
        for i in range(N):
            for j in range(N):
                if group[i][j] == c: # 같은 그룹
                    if B[i][j] > max_B:
                        max_B = B[i][j]
                        max_i = i
                        max_j = j
        leader.append([max_i, max_j, F[max_i][max_j], B[max_i][max_j]])
        leader_coord.append((max_i, max_j))

    # 그룹원 신앙심 -1, 대표 신앙심 + 그룹원 수
    for c in range(1, group_cnt + 1):
        for i in range(N):
            for j in range(N):
                if group[i][j] == c:
                    x, y = leader[c - 1][0], leader[c - 1][1]
                    if group[i][j] not in leader:
                        B[i][j] -= 1
                        B[x][y] += 1

    for l in leader:
        l[3] = B[l[0]][l[1]]

    # print('점심')
    # for i in B:
    #     print(i)
    # print()

    # 저녁
    # 전파 순서 정렬
    sorting_group = sorting(leader)
    leader_flag = [[0] * N for _ in range(N)]

    # print('대표자 전파 순서')
    # print(sorting_group)
    # print()

    for l in sorting_group:
        # print((l[0], l[1]))
        x, y = l[0], l[1]               # 리더 현재 위치
        if leader_flag[x][y] == 1:      # 리더가 전파 당했다면
            # print('리더가 전파당해 전파 x')
            # print()
            continue
        energy = l[3] - 1               # 간절함: B - 1
        dx, dy = direction[l[3] % 4]    # 리더 이동 방향
        # print(f'이동 방향: ({dx}, {dy})')
        B[l[0]][l[1]] = 1               # 리더 신앙심: 1
        nx, ny = x, y
        
        while True:
            nx += dx                # 리더 이동 위치
            ny += dy
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N or energy == 0:
                break
            
            # print(f'이동 위치: ({nx}, {ny})')
            # print(f'기존 간절함: {energy}')

            if F[nx][ny] == l[2]:
                continue
            else:
                if energy > B[nx][ny]:  # 강한 전파
                    if (nx, ny) in leader_coord: # 리더가 전파 받았다면
                        leader_flag[nx][ny] = 1
                        
                    F[nx][ny] = l[2]
                    energy -= (B[nx][ny] + 1)
                    B[nx][ny] += 1
                    
                    # print(f'강한전파 이후 남은 간절함: {energy}')
                    
                    if energy == 0:
                        break
                else:                   # 약한 전파
                    if (nx, ny) in leader_coord: # 리더가 전파 받았다면
                        leader_flag[nx][ny] = 1
                    
                    present_food = F[nx][ny]
                    leader_food = l[2]
                    new_food = ''
                    
                    # 이렇게 조건 길게 나열하는 방법 X
                    # if (F[nx][ny] == 'T' and l[2] == 'CM') or (F[nx][ny] == 'C' and l[2] == 'TM') or (F[nx][ny] == 'M' and l[2] == 'TC') or (F[nx][ny] == 'CM' and l[2] == 'T') or (F[nx][ny] == 'TM' and l[2] == 'C') or (F[nx][ny] == 'TC' and l[2] == 'M') or (F[nx][ny] == 'TC' and l[2] == 'CM') or (F[nx][ny] == 'TC' and l[2] == 'TM') or (F[nx][ny] == 'TC' and l[2] == 'M'):
                    #     F[nx][ny] = 'TCM'
                    # elif (F[nx][ny] == 'T' and l[2] == 'C') or (F[nx][ny] == 'C' and l[2] == 'T'):
                    #     F[nx][ny] = 'TC'
                    # elif (F[nx][ny] == 'T' and l[2] == 'M') or (F[nx][ny] == 'M' and l[2] == 'T'):
                    #     F[nx][ny] = 'TM'
                    # elif (F[nx][ny] == 'C' and l[2] == 'M') or (F[nx][ny] == 'M' and l[2] == 'C'):
                    #     F[nx][ny] = 'CM'

                    # !! 해결 방법 !!
                    if 'T' in present_food or 'T' in leader_food:
                        new_food += 'T'
                    if 'C' in present_food or 'C' in leader_food:
                        new_food += 'C'
                    if 'M' in present_food or 'M' in leader_food:
                        new_food += 'M'

                    F[nx][ny] = new_food               
                    B[nx][ny] += energy
                    
                    # print(f'약한전파: {energy}')
                    
                    energy = 0
                    break
                
        # for i in B:
        #     print(i)
        # print()
        
        # for i in F:
        #     print(i) 
        # print() 
        
    B_list = []
    for food in ['TCM', 'TC', 'TM', 'CM', 'M', 'C', 'T']:
        res = 0
        for i in range(N):
            for j in range(N):
                if F[i][j] == food:
                    res += B[i][j]
        B_list.append(res)

    for i in B_list:
        print(i, end= ' ')
    print()