import sys
from collections import deque

input = sys.stdin.readline

def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 1

    while q:
        si, sj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = si + di, sj + dj

            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                continue

            if v[ni][nj] == 0 and grid[ni][nj] != 0:
                v[ni][nj] = 1
                q.append((ni, nj))


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 처음에 빙산이 있는 좌표들만 모아두기
ice = []
for i in range(n):
    for j in range(m):
        if grid[i][j] != 0:
            ice.append((i, j))

time = 0

while True:
    # 1) 빙산이 아예 없으면 -> 끝까지 분리 안 됐으니 0
    if not ice:
        print(0)
        break

    # 2) 현재 빙산이 몇 덩어리인지 체크
    v = [[0] * m for _ in range(n)]

    # 아무 빙산 좌표 하나에서 BFS 시작
    si, sj = ice[0]
    bfs(si, sj)

    # ice 중에서 방문 안 된 칸이 있으면 -> 덩어리가 2개 이상
    separated = False
    for i, j in ice:
        if v[i][j] == 0:   # 같은 덩어리가 아님
            separated = True
            break

    if separated:
        print(time)        # 지금까지 지난 년수
        break

    # 3) 아직 한 덩어리면 -> 1년 만큼 녹이기

    # 각 빙산 칸별로 주변 바다 개수를 계산
    # (딕셔너리나 리스트에 저장했다가 한 번에 반영)
    melt_info = []   # (i, j, 새 높이)
    for i, j in ice:
        sea = 0
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if grid[ni][nj] == 0:
                    sea += 1
        nh = grid[i][j] - sea
        if nh < 0:
            nh = 0
        melt_info.append((i, j, nh))

    # 그 결과를 grid에 반영하면서, 다음 해용 ice 리스트 재구성
    new_ice = []
    for i, j, nh in melt_info:
        grid[i][j] = nh
        if nh > 0:
            new_ice.append((i, j))
    ice = new_ice

    time += 1
