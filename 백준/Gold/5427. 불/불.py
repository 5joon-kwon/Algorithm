import sys
from collections import deque
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

def find_start():
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '@':
                return i, j

def find_fire():
    fires = []
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '*':
                fires.append((i, j))
    return fires

def in_range(i, j):
    return 0 <= i < h and 0 <= j < w

# fmap: 불 도착 시간(초). -1이면 아직 불 안 옴
def fire_bfs(fire, fmap):
    q = deque()
    for fi, fj in fire:
        q.append((fi, fj))
        fmap[fi][fj] = 0

    while q:
        i, j = q.popleft()
        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = i + di, j + dj
            if in_range(ni, nj) and maps[ni][nj] != '#' and fmap[ni][nj] == -1:
                fmap[ni][nj] = fmap[i][j] + 1
                q.append((ni, nj))

# v: 사람 도착 시간(초). -1이면 아직 방문 안 함
def bfs(si, sj, v, fmap):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 0  # 시작 시간 0초

    while q:
        i, j = q.popleft()
        t = v[i][j]

        for di, dj in ((1,0), (0,1), (-1,0), (0,-1)):
            ni, nj = i + di, j + dj
            nt = t + 1

            # 다음 칸이 맵 밖이면 탈출 성공
            if not in_range(ni, nj):
                return nt

            # 벽이면 못 감
            if maps[ni][nj] == '#':
                continue

            # 이미 방문했으면 스킵
            if v[ni][nj] != -1:
                continue

            # 불이 먼저(또는 동시에) 도착하면 못 감
            if fmap[ni][nj] != -1 and fmap[ni][nj] <= nt:
                continue

            v[ni][nj] = nt
            q.append((ni, nj))

    return "IMPOSSIBLE"
            
testcase = int(input())
for tc in range(testcase):
    w, h = map(int, input().split())
    maps = [list(input()) for _ in range(h)]
    res = 0
    
    fmap = [[-1] * w for _ in range(h)]
    v = [[-1] * w for _ in range(h)]
    
    si, sj = find_start()
    fire = find_fire()
    
    fire_bfs(fire, fmap)

    print(bfs(si, sj, v, fmap))