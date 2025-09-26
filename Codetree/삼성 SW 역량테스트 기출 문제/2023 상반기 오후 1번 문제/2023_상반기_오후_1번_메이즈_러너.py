def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def rotate_wall_minus(si, sj, rarr, L):
    for i in range(L):
        for j in range(L):
            rarr[si + i][sj + j] = arr[si + L - 1 - j][sj + i]
            if rarr[si + i][sj + j] > 0:
                rarr[si + i][sj + j] -= 1
    return rarr

def in_range(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False

def find_square(arr):
    min_dist = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                min_dist = min(min_dist, max(abs(i - ei), abs(j - ej)))

    for si in range(N - min_dist):
        for sj in range(N - min_dist):
            if si <= ei <= si + min_dist and sj <= ej <= sj + min_dist:
                for i in range(si, si + min_dist + 1):
                    for j in range(sj, sj + min_dist + 1):
                        if -11 < arr[i][j] < 0:
                            return si, sj, min_dist + 1

def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for m in range(1, M + 1):
    i, j = map(lambda x: int(x) - 1, input().split())
    arr[i][j] = -1

ei, ej = map(lambda x: int(x) - 1, input().split())
arr[ei][ej] = -11

ans = 0
cnt = M
for _ in range(K):
    narr = [x[:] for x in arr]
    for ci in range(N):
        for cj in range(N):
            if -11 < arr[ci][cj] < 0:
                dist = distance(ci, cj, ei, ej)
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = ci + di, cj + dj
                    if in_range(ni, nj) and arr[ni][nj] <= 0 and dist > distance(ni, nj, ei, ej):
                        ans += arr[ci][cj]
                        narr[ci][cj] -= arr[ci][cj]
                        if arr[ni][nj] == -11:
                            cnt += arr[ci][cj]
                        else:
                            narr[ni][nj] += arr[ci][cj]
                        break
    arr = narr

    if cnt == 0:
        break

    si, sj, L = find_square(arr)

    rarr = [x[:] for x in arr]
    arr = rotate_wall_minus(si, sj, rarr, L)

    ei, ej = find_exit(arr)

print(-ans)
print(ei + 1, ej + 1)