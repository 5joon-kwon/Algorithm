# NxN 격자 1~10 숫자
# 1. 인접한 숫자들 같으면 동일 그룹
# 2. 그룹 쌍의 조화 : (a에 속한 칸의 수 + b에 속한 칸의 수) x (a의 숫자 x b의 숫자 x 맞닿아 있는 변의 수)
# 3. 초기 예술 점수 : 서로 맞닿아 있는 두 개의 그룹 쌍의 조화 총합
# 4. 중앙 (i:)(:j) 십자 반시계 90 회전 나머지 + 4 부분 시계 90 회전 동시 진행
# 5. 회전 후 예술 점수 3. 처럼 구하기
# 6. 초기, 1 ~ 3회전 후 예술 점수 출력

def calculate():
    visit = [[0] * n for _ in range(n)] # 방문확인

    # [1-1] 미방문 숫자를 만나면 BFS(): 같은그룹 좌표를 set에 추가
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                group_num.append(grid[i][j])
                group_coord.append(set())
                bfs(visit, i, j)

    # [1-2] 각 그룹간 점수 계산(누적)
    num = len(group_num) # 그룹 수
    ans = 0
    for i in range(0, num - 1): # 가능한 모든 조합 구하는 방법
        for j in range(i + 1, num):
            for ai, aj in group_coord[i]: # 그룹 a
                for ni, nj in ((ai + 1, aj), (ai - 1, aj), (ai, aj - 1), (ai, aj + 1)): # 맞닿아 있는 변의 수는 반복문으로 덧셈 계산
                    if (ni, nj) in group_coord[j]: # 인접 조건
                        ans += (len(group_coord[i]) + len(group_coord[j])) * (group_num[i] * group_num[j])
    return ans

from collections import deque
def bfs(visit, si, sj):
    queue = deque()
    queue.append((si, sj))
    visit[si][sj] = 1
    group_coord[-1].add((si, sj)) # 가장 최근 set 에 좌표 추가

    while queue:
        i, j = queue.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and visit[ni][nj] == 0 and grid[ni][nj] == grid[i][j]:
                queue.append((ni, nj))
                visit[ni][nj] = 1
                group_coord[-1].add((ni, nj)) # 가장 최근 set 에 좌표 추가

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

m = n // 2
res = 0
for k in range(4):
    group_coord = []
    group_num = []
    res += calculate()

    if k == 3: # 3번째 턴이면 회전 필요 없음
        break

    # [2] 회전시키기: '+' 반시계 회전, 사각형들 시계방향
    ngrid = [[0] * n for _ in range(n)]
    for i in range(n):
        ngrid[i][m] = grid[m][n - 1 - i]
    for j in range(n):
        ngrid[m][j] = grid[j][m]
    for (si, sj) in ((0, 0), (0, m + 1), (m + 1, 0), (m + 1, m + 1)):
        for i in range(m):
            for j in range(m):
                ngrid[si + i][sj + j] = grid[si + m - 1 - j][sj + i]

    grid = ngrid

print(res)
