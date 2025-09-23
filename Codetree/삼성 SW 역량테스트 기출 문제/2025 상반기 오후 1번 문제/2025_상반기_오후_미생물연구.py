from collections import deque

N, Q = map(int, input().split())
arr = [[0] * N for _ in range(N)]

def arr_input(q):
    sj, si, ej, ei = map(int, input().split())
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = q

def bfs(visited, si, sj):
    q = deque()
    sn = arr[si][sj]
    res = []

    q.append([si, sj])
    visited[si][sj] = sn
    res.append(sn)
    res.append([si, sj])

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] == sn:
                q.append([ni, nj])
                visited[ni][nj] = sn
                res.append([ni, nj])

    return res

def group():
    visited = [[0] * N for _ in range(N)]
    glist = []

    for si in range(N):
        for sj in range(N):
            if visited[si][sj] == 0 and arr[si][sj] > 0:
                tlist = bfs(visited, si, sj)
                glist.append(tlist)

    return glist

def del_sort(glist):
    del_set = set()
    for i in range(len(glist) - 1):
        for j in range(i + 1, len(glist)):
            if glist[i][0] == glist[j][0]:
                del_set.add(i)
                del_set.add(j)

    for i in range(len(glist) - 1, -1, -1):
        if i in del_set:
            glist.pop(i)

    glist.sort(key = lambda x: (-len(x), x[0]))

    for li in glist:
        mi, mj = N, N
        for ci, cj in li[1:]:
            mi = min(ci, mi)
            mj = min(cj, mj)

        for i in range(1, len(li)):
            li[i][0] -= mi
            li[i][1] -= mj

    return glist

def check(narr, li):
    for j in range(N):
        for i in range(N):
            for ci, cj in li:
                if i + ci >= N or j + cj >= N or narr[i + ci][j + cj] != 0:
                    break
            else:
                return i, j

    return -1, -1

def move(glist):
    narr = [[0] * N for _ in range(N)]

    for li in glist:
        sn = li[0]
        mi, mj = check(narr, li[1:])
        if (mi, mj) != (-1, -1):
            for ci, cj in li[1:]:
                narr[mi + ci][mj + cj] = sn

    return narr

def bfs_adj(visited, si, sj):
    q = deque()
    q.append([si, sj])
    visited[si][sj] = 1
    cnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[si][sj] == arr[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = 1
                cnt += 1

    return cnt

def bfs_score(visited, i, j):
    q = deque()
    w = [[0] * N for _ in range(N)]
    cnts = []

    q.append([i, j])
    visited[i][j] = 1
    mycnt = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if arr[ci][cj] == arr[ni][nj]:
                    q.append([ni, nj])
                    visited[ni][nj] = 1
                    mycnt += 1
                elif arr[ni][nj] != 0 and w[ni][nj] == 0:
                    diff = bfs_adj(w, ni, nj)
                    cnts.append(diff)

    ans = 0
    for cnt in cnts:
        ans += cnt * mycnt

    return ans

def score(arr):
    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if (visited[i][j] == 0 and arr[i][j] != 0):
                s = bfs_score(visited, i, j)
                ans += s

    return ans

for q in range(1, Q + 1):
    arr_input(q)

    glist = group()

    glist = del_sort(glist)

    arr = move(glist)

    ans = score(arr)

    print(ans)