from collections import deque

def find_3d_start():
    for i in range(M):
        for j in range(M):
            if arr3[4][i][j] == 2:
                return 4, i, j

def find_2d_end():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 4:
                arr[i][j] = 0
                return i, j

def find_3d_base():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                return i, j

def find_3d_end_2d_start():
    bi, bj = find_3d_base()

    for i in range(bi, bi + M):
        for j in range(bj, bj + M):
            if arr[i][j] != 3:
                continue

            if arr[i][j + 1] == 0:
                return 0, M - 1, (M - 1) - (i - bi), i, j + 1
            elif arr[i][j - 1] == 0:
                return 1, M - 1, i - bi, i, j - 1
            elif arr[i + 1][j] == 0:
                return 2, M - 1, j - bj, i + 1, j
            elif arr[i - 1][j] == 0:
                return 3, M - 1, (M - 1) - (j - bj), i - 1, j

    return -1

lnext = {0:2, 2:1, 1:3, 3:0}
rnext = {0:3, 2:0, 1:2, 3:1}
def bfs_3d(sk, si, sj, ek, ei, ej):
    q = deque()
    # 동, 서, 남, 북, 윗면
    visited = [[[0] * M for _ in range(M)] for _ in range(5)]

    q.append((sk, si, sj))
    visited[sk][si][sj] = 0

    while q:
        ck, ci, cj = q.popleft()

        if (ck, ci, cj) == (ek, ei, ej):
            return visited[ck][ci][cj]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj

            if ni < 0:
                if ck == 4:
                    nk, ni, nj = 3, 0, (M - 1) - cj
                elif ck == 0:
                    nk, ni, nj = 4, (M - 1) - cj, M - 1
                elif ck == 1:
                    nk, ni, nj = 4, cj, 0
                elif ck == 2:
                    nk, ni, nj = 4, M - 1, cj
                elif ck == 3:
                    nk, ni, nj = 4, 0, (M - 1) - cj
            elif ni >= M:
                if ck == 4:
                    nk, ni, nj = 2, 0, cj
                else:
                    continue
            elif nj < 0:
                if ck == 4:
                    nk, ni, nj = 1, 0, ci
                else:
                    nk, ni, nj = lnext[ck], ci, M - 1
            elif nj >= M:
                if ck == 4:
                    nk, ni, nj = 0, 0, (M - 1) - ci
                else:
                    nk, ni, nj = rnext[ck], ci, 0
            else:
                nk = ck

            if visited[nk][ni][nj] == 0 and arr3[nk][ni][nj] == 0:
                q.append((nk, ni, nj))
                visited[nk][ni][nj] = visited[ck][ci][cj] + 1

    return -1

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
def wall_2d():
    time = [[401] * N for _ in range(N)]
    for wi, wj, wd, wv in time_loc:
        time[wi][wj] = 1
        for m in range(1, N + 1):
            wi, wj = wi + di[wd], wj + dj[wd]
            if 0 <= wi < N and 0 <= wj < N and arr[wi][wj] == 0 and (wi, wj) != (ei, ej):
                if time[wi][wj] > wv * m:
                    time[wi][wj] = wv * m
            else:
                break

    return time

def bfs_2d(wall, dist_3d, si, sj, ei, ej):
    q = deque()

    q.append((si, sj))
    wall[si][sj] = dist_3d + 1

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            return wall[ci][cj]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and wall[ci][cj] + 1 < wall[ni][nj]:
                q.append((ni, nj))
                wall[ni][nj] = wall[ci][cj] + 1

    return -1

# -----------------------------------------------------------------

N, M, F = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 동, 서, 남, 북, 윗면
arr3 = [[list(map(int, input().split())) for _ in range(M)] for _ in range(5)]
time_loc = [list(map(int, input().split())) for _ in range(F)]

sk3d, si3d, sj3d = find_3d_start()
ei, ej = find_2d_end()
ek3d, ei3d, ej3d, si, sj = find_3d_end_2d_start()

dist_3d = bfs_3d(sk3d, si3d, sj3d, ek3d, ei3d, ej3d)

wall = []
if dist_3d != -1:
    wall = wall_2d()
    dist_2d = bfs_2d(wall, dist_3d, si, sj, ei, ej)
    print(dist_2d)
else:
    print(-1)