import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

from collections import deque

def find_things():
    si, sj = 0, 0
    waters = []
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'S':
                si, sj = i, j
            elif maps[i][j] == '*':
                waters.append((i, j))
    
    return si, sj, waters

def in_range(i, j):
    return 0 <= i < h and 0 <= j < w

# 매 분 물 상하좌우 빈 칸으로 확장 (D, X로 못감)
def water_bfs(waters, wmap):
    q = deque(waters)
    for i, j in waters:
        wmap[i][j] = 0
    
    while q:
        wi, wj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = wi + di, wj + dj
            if in_range(ni, nj) and wmap[ni][nj] == -1 and maps[ni][nj] != 'X' and maps[ni][nj] != 'D':
                q.append((ni, nj))
                wmap[ni][nj] = wmap[wi][wj] + 1

# 매 분 고슴도치 상하좌우 (*, X, 물이 찰 예정인 칸으로 못감)
def bfs(i, j, hmap):
    q = deque([(i, j)])
    hmap[i][j] = 0

    while q:
        si, sj = q.popleft()
        time = hmap[si][sj]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = si + di, sj + dj
            if not in_range(ni, nj):
                continue

            if hmap[ni][nj] != -1:
                continue

            if maps[ni][nj] in ('X', '*'):
                continue

            if maps[ni][nj] == 'D':
                return time + 1
            
            if wmap[ni][nj] != -1 and time + 1 >= wmap[ni][nj]:
                continue

            q.append((ni, nj))
            hmap[ni][nj] = time + 1

    # 못들어가면 KAKTUS 출력
    return 'KAKTUS'

h, w = map(int, input().split())
maps = [list(input()) for _ in range(h)]

# . : 빈 곳
# * : 물
# X : 돌
# D : 출구
# S : 시작
si, sj, waters = find_things()
wmap = [[-1] * w for _ in range(h)]
hmap = [[-1] * w for _ in range(h)]

water_bfs(waters, wmap)
print(bfs(si, sj, hmap))