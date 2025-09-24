from collections import deque

def in_range(ni, nj):
    if (0 <= ni < N and 0 <= nj < N):
        return True
    return False

def find_route(si, sj, ei, ej):
    q = deque()
    visited = [[0] * N for _ in range(N)]
    q.append((si, sj))
    visited[si][sj] = (si, sj)

    while q:
        ci, cj = q.popleft()

        if (ci, cj) == (ei, ej):
            path = []
            i, j = visited[ci][cj]

            while (i, j) != (si, sj):
                path.append((i, j))
                i, j = visited[i][j]

            return path[::-1]

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and visited[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = (ci, cj)

    return -1

def mark_line(cview, i, j, dir):
    while in_range(i, j):
        cview[i][j] = 2
        i, j = i + di[dir], j + dj[dir]

#     상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
#      0,  1,  2,   3,  4,   5,  6,   7
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def mark_safe(cview, si, sj, dir, dia):
    mark_line(cview, si + di[dir], sj + dj[dir], dir)

    ni, nj = si + di[dia], sj + dj[dia]
    while in_range(ni, nj):
        mark_line(cview, ni, nj, dir)
        ni, nj = ni + di[dia], nj + dj[dia]

def make_stone(wmap, mi, mj, dir):
    cview = [[0] * N for _ in range(N)]
    stone_cnt = 0

    ni, nj = mi + di[dir], mj + dj[dir]
    while in_range(ni, nj):
        cview[ni][nj] = 1

        if wmap[ni][nj] > 0:
            stone_cnt += wmap[ni][nj]
            mark_line(cview, ni + di[dir], nj + dj[dir], dir)
            break

        ni, nj = ni + di[dir], nj + dj[dir]

    for dia in ((dir - 1) % 8, (dir + 1) % 8):
        si, sj = mi + di[dia], mj + dj[dia]
        while in_range(si, sj):
            if cview[si][sj] == 0 and wmap[si][sj] > 0:
                cview[si][sj] = 1
                stone_cnt += wmap[si][sj]
                mark_safe(cview, si, sj, dir, dia)
                break

            nei, nej = si, sj
            while in_range(nei, nej):
                if cview[nei][nej] != 0:
                    break

                cview[nei][nej] = 1

                if wmap[nei][nej] > 0:
                    stone_cnt += wmap[nei][nej]
                    mark_safe(cview, nei, nej, dir, dia)
                    break

                nei, nej = nei + di[dir], nej + dj[dir]

            si, sj = si + di[dia], sj + dj[dia]

    return cview, stone_cnt

def move_men(view, mi, mj):
    move, attack = 0, 0

    for dirs in (((-1,0),(1,0),(0,-1),(0,1)), ((0,-1),(0,1),(-1,0),(1,0))):
        for idx in range(len(war) - 1, -1, -1):
            wi, wj = war[idx]
            if view[wi][wj] == 1:
                continue

            dist = abs(wi - mi) + abs(wj - mj)
            for di, dj in dirs:
                ni, nj = wi + di, wj + dj
                if in_range(ni, nj) and view[ni][nj] != 1 and dist > abs(ni - mi) + abs(nj - mj):
                    if (ni, nj) == (mi, mj):
                        attack += 1
                        war.pop(idx)
                    else:
                        war[idx] = [ni, nj]
                    move += 1
                    break
    return move, attack

# =================================================================

N, M = map(int, input().split())
si, sj, ei, ej = map(int, input().split())
loc = list(map(int, input().split()))

war = []
for i in range(0, M * 2, 2):
    war.append([loc[i], loc[i + 1]])

arr = [list(map(int, input().split())) for _ in range(N)]

route = find_route(si, sj, ei, ej)

if route == -1:
    print(-1)
else:
    for mi, mj in route:
        move_cnt, attack_cnt = 0, 0

        for i in range(len(war) - 1, -1, -1):
            if war[i] == [mi, mj]:
                war.pop(i)

        wmap = [[0] * N for _ in range(N)]
        for wi, wj in war:
            wmap[wi][wj] += 1

        max_stone = -1
        view = []
        for dir in (0, 4, 6, 2):
            dview, dstone = make_stone(wmap, mi, mj, dir)
            if max_stone < dstone:
                max_stone = dstone
                view = dview

        move_cnt, attack_cnt = move_men(view, mi, mj)
        print(move_cnt, max_stone, attack_cnt)
    print(0)