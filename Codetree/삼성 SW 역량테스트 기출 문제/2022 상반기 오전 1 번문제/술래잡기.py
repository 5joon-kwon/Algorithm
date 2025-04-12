# nxn 격자, 술래(2//m, 2//m), 도망자 m명 (상하: 아래쪽으로 시작 or 좌우: 오른쪽으로 시작)
# 나무 h개 (초기에 도망자와 겹칠 수 있음)
# 도망자 m명 동시에 움직이고, 술래 움직이고 : 1턴 k 번 반복
# 도망자는 술래랑 거리가 3 이하이면 이동
# 범위 내, 이동할 곳에 술래 있으면 이동x, 나무로도 이동 가능)
# 범위 벗어나면, 방향을 반대로 돌고 술래 없으면 이동
# 술래는 중심에서 달팽이(시계)로 이동, 끝이면 중심으로(반시계)로 이동 (중심 or 방향 틀어지는 지점이면 방향 바로 틈)
# 방향에서 현재칸 포함 3칸 시야 내에 있는 도망자 잡음 but, 나무 있으면 못잡음
# 점수 : t턴 x 잡은 도망자 수

n, m, h, k = map(int, input().split())
runner = [list(map(int, input().split())) for _ in range(m)] # i, j, d (1: 좌우, 2: 상하)
tree = set()
for _ in range(h):
    x, y = map(int, input().split())
    tree.add((x, y))

rdi = [0, 0, 1, -1] # 도망자 좌 우(1) 하(2) 상
rdj = [-1, 1, 0, 0]
opp = {0: 1, 1: 0, 2: 3, 3: 2} # 범위 밖이면 반대로

cdi = [-1, 0, 1, 0] # 술래 상우하좌 순서로 이동
cdj = [0, 1, 0, -1]
mid = (n + 1) // 2
ci, cj, cdr = mid, mid, 0 # 술래 초기 위치, 이동 방향

# 중심 -> 바깥 달팽이
max_cnt = 1 # 초기 최대 이동 거리
cnt = 0 # 초기 이동 거리
flag = 0 # 두 차례마다 방향 회전
val = 1 # 방향 제어 및 이동 거리 변화

ans = 0
for t in range(1, k + 1):
    # [1] 도망자의 이동(arr)
    for idx in range(len(runner)):
        if abs(ci - runner[idx][0]) + abs(cj - runner[idx][1]) <= 3:
            ni, nj = runner[idx][0] + rdi[runner[idx][2]], runner[idx][1] + rdj[runner[idx][2]]
            if 1 <= ni <= n and 1 <= nj <= n:
                if (ni, nj) != (ci, cj): # 술래 안만나면
                    runner[idx][0], runner[idx][1] = ni, nj
            else:
                runner[idx][2] = opp[runner[idx][2]]
                ni, nj = runner[idx][0] + rdi[runner[idx][2]], runner[idx][1] + rdj[runner[idx][2]]
                if (ni, nj) != (ci, cj):
                    runner[idx][0], runner[idx][1] = ni, nj

    # [2] 술래의 이동
    cnt += 1
    ci, cj = ci + cdi[cdr], cj + cdj[cdr]
    if (ci, cj) == (mid, mid): # 중심 -> 바깥
        max_cnt, cnt, flag, val = 1, 0, 0, 1
        cdr = 0
    elif (ci, cj) == (1, 1): # 바깥 -> 중심
        max_cnt, cnt, flag, val = n, 1, 1, -1
        cdr = 2
    else:
        if cnt == max_cnt:
            cnt = 0
            cdr = (cdr + val) % 4 # val에 따라 시계, 반시계
            if flag == 0: # 처음 꺾이면
                flag = 1
            else:
                flag = 0
                max_cnt += val # 두 번째로 꺾이면 val에 따라 max_cnt 늘리거나 줄이거나

    # [3] 도망자 잡기(술래자리 포함 3칸: 나무가없는 도망자면 잡힘!)
    cset = {(ci, cj), (ci + cdi[cdr], cj + cdj[cdr]), (ci + cdi[cdr]*2, cj + cdj[cdr]*2)}
    for idx in range(len(runner) - 1, -1, -1): # 삭제는 뒤에서부터
        if (runner[idx][0], runner[idx][1]) in cset and (runner[idx][0], runner[idx][1]) not in tree:
            runner.pop(idx)
            ans += t

    if not runner: # 비어있으면
        break

print(ans)