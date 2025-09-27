from collections import deque

n, m, h, k = map(int, input().split())
runner = [list(map(int, input().split())) for _ in range(m)]
trees = set()
for _ in range(h):
    i, j = map(int, input().split())
    trees.add((i, j))
     
tdi = [-1, 0, 1, 0]
tdj = [0, 1, 0, -1]
max_cnt, cnt, flag, val = 1, 0, 0, 1
mid = (n + 1) // 2
ti, tj, td = mid, mid, 0

rdi = [0, 0, 1, -1]
rdj = [-1, 1, 0, 0]
opd = {0:1, 1:0, 2:3, 3:2}

ans = 0
for turn in range(1, k + 1):
    for i in range(len(runner)):
        ri, rj, rd = runner[i][0], runner[i][1], runner[i][2]
        if abs(ri - ti) + abs(rj - tj) <= 3:
            ni, nj = ri + rdi[rd], rj + rdj[rd]
            if 1 <= ni <= n and 1 <= nj <= n:
                if (ni, nj) != (ti, tj):
                    runner[i] = [ni, nj, rd]
            else:
                rd = opd[rd]
                ni, nj = ri + rdi[rd], rj + rdj[rd]
                if (ni, nj) != (ti, tj):
                    runner[i] = [ni, nj, rd]
    
    
    cnt += 1
    ti, tj = ti + tdi[td], tj + tdj[td]
    
    if (ti, tj) == (1, 1):
        max_cnt, cnt, flag, val = n, 1, 1, -1
        td = 2
    elif (ti, tj) == (mid, mid):
        max_cnt, cnt, flag, val = 1, 0, 0, 1
        td = 0
        
    if cnt == max_cnt:
        cnt = 0
        td = (td + val) % 4
        
        if flag == 1:
            flag = 0
            max_cnt += val 
        else:
            flag = 1 
    
    tset = set(((ti, tj), (ti + tdi[td], tj + tdj[td]), (ti + 2 * tdi[td], tj + 2 * tdj[td])))
    for idx in range(len(runner) - 1, -1, -1):
        mi, mj, _ = runner[idx]
        if (mi, mj) in trees:
            continue
        
        if (mi, mj) in tset:
            runner.pop(idx)
            ans += turn
        
    if len(runner) == 0:
        break

print(ans)