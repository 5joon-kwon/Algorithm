from collections import deque

def distance(ri, rj, si, sj):
    return (ri - si) ** 2 + (rj - sj) ** 2

def target_santa():
    min_dist = 2 * N ** 2
    mlist = []

    for idx in range(1, P + 1):
        if alive[idx] == 0:
            continue

        sn, si, sj = santa[idx]
        dist = distance(ri, rj, si, sj)
        if min_dist > dist:
            min_dist = dist
            mlist = [(si, sj, idx)]
        elif min_dist == dist:
            mlist.append((si, sj, idx))

    mlist.sort(reverse=True)
    return mlist[0]

def in_range(i, j):
    if 0 <= i < N and 0 <= j < N:
        return True
    return False

def move_santa(tn, ti, tj, dri, drj, score):
    q = deque()
    q.append((tn, ti, tj, score))

    while q:
        cn, ci, cj, cscore = q.popleft()
        ni, nj = ci + dri * cscore, cj + drj * cscore

        if in_range(ni, nj):
            if arr[ni][nj] == 0:
                arr[ni][nj] = cn
                santa[cn] = [cn, ni, nj]
                return
            else:
                q.append((arr[ni][nj], ni, nj, 1))
                arr[ni][nj] = cn
                santa[cn] = [cn, ni, nj]
        else:
            alive[cn] = 0
            return

# ----------------------------------------------------------

N, M, P, C, D = map(int, input().split())
ri, rj = map(lambda x: int(x) - 1, input().split())
arr = [[0] * N for _ in range(N)]
arr[ri][rj] = -1

santa = [[0, 0, 0]]
for i in range(1, P + 1):
    n, i, j = map(int, input().split())
    santa.append([n, i - 1, j - 1])
    arr[i - 1][j - 1] = n
santa.sort()

score = [0] * (P + 1)
alive = [1] * (P + 1)
alive[0] = 0
wake_turn = [1] * (P + 1)

for turn in range(1, M + 1):
    if alive.count(1) == 0:
        break

    ti, tj, tn = target_santa()
    rdi, rdj = 0, 0

    if ri > ti:
        rdi = -1
    elif ri < ti:
        rdi = 1

    if rj > tj:
        rdj = -1
    elif rj < tj:
        rdj = 1

    arr[ri][rj] = 0
    ri, rj = ri + rdi, rj + rdj
    arr[ri][rj] = -1

    if (ri, rj) == (ti, tj):
        score[tn] += C
        wake_turn[tn] = turn + 2
        move_santa(tn, ti, tj, rdi, rdj, C)

    for idx in range(1, P + 1):
        sn, si, sj = santa[idx]

        if alive[idx] == 0:
            continue

        if wake_turn[idx] > turn:
            continue

        min_dist = distance(ri, rj, si, sj)
        mi, mj, mdi, mdj = 0, 0, 0, 0
        mflag = False

        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = si + di, sj + dj
            if in_range(ni, nj) and arr[ni][nj] <= 0:
                n_dist = distance(ri, rj, ni, nj)
                if min_dist > n_dist:
                    min_dist = n_dist
                    mi, mj = ni, nj
                    mdi, mdj = di, dj
                    mflag = True

        if not mflag:
            continue

        if (mi, mj) == (ri, rj):
            score[idx] += D
            wake_turn[idx] = turn + 2
            arr[si][sj] = 0
            move_santa(idx, mi, mj, -mdi, -mdj, D)
        else:
            arr[si][sj] = 0
            arr[mi][mj] = idx
            santa[idx] = [idx, mi, mj]

    for i in range(1, P + 1):
        if alive[i] == 1:
            score[i] += 1

print(*score[1:])