from collections import deque

def bfs(visited, i, j):
    q = deque()
    food = farr[i][j]
    blist = []

    q.append([i, j])
    visited[i][j] = food
    blist.append([-barr[i][j], i, j])

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and farr[ni][nj] == food:
                q.append([ni, nj])
                visited[ni][nj] = food
                blist.append([-barr[ni][nj], ni, nj])

    blist.sort()
    _, bi, bj = blist[0]
    barr[bi][bj] += len(blist)
    return bi, bj

group_order = {4:1, 2:1, 1:1, 3:2, 5:2, 6:2, 7:3}
def group():
    boss_list = []
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bi, bj = bfs(visited, i, j)
                bfood = farr[bi][bj]
                boss_list.append([group_order[bfood], -barr[bi][bj], bi, bj])

    return boss_list

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def move(boss_list):
    moved = set()
    for _, cp, ci, cj in boss_list:
        if (ci, cj) in moved:
            continue

        cp = -cp
        di, dj = dir[cp % 4]
        power = cp - 1
        barr[ci][cj] = 1
        cfood = farr[ci][cj]

        while True:
            ci, cj = ci + di, cj + dj
            if not (0 <= ci < N and 0 <= cj < N) or power <= 0:
                break

            if farr[ci][cj] != cfood:
                moved.add((ci, cj))
                if power > barr[ci][cj]:
                    farr[ci][cj] = cfood
                    barr[ci][cj] += 1
                    power -= barr[ci][cj]
                else:
                    farr[ci][cj] |= cfood
                    barr[ci][cj] += power
                    break

N, T = map(int, input().split())
farr = [list(input()) for _ in range(N)]
barr = [list(map(int, input().split())) for _ in range(N)]
mapping = {'T':4, 'C':2, 'M': 1}

for i in range(N):
    for j in range(N):
        farr[i][j] = mapping[farr[i][j]]

for t in range(T):
    boss_list = group()
    boss_list.sort()

    move(boss_list)

    ans = [0] * 7
    for idx, food in enumerate((7, 6, 5, 3, 1, 2, 4)):
        for i in range(N):
            for j in range(N):
                if farr[i][j] == food:
                    ans[idx] += barr[i][j]

    print(*ans)