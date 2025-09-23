from collections import deque
def bfs(v, si, sj):
    q = deque()
    food = farr[si][sj]
    blst = []

    q.append((si,sj))
    v[si][sj]=food
    blst.append([-barr[si][sj],si,sj])

    while q:
        ci,cj = q.popleft()
        # 네방향, 범위내, 미방문, 조건(==food)
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and farr[ni][nj]==food:
                q.append((ni,nj))
                v[ni][nj]=food
                blst.append([-barr[ni][nj],ni,nj])

    # -신앙심, 행, 열 : 대표자 리턴
    blst.sort()
    _,bi,bj = blst[0]
    barr[bi][bj]+=len(blst)     # 대표자는 그룹인원수만큼 신앙심+
    return bi,bj                # boss i,j좌표 리턴

# [1] 대표자리스트(전파할 우선순위) [우선순위, -신앙심, 행, 열]
# 단일: 민트(4),초코(2),우유(1), 이중: 초코우유(3),민트우유(5),민트초코(6), 3중: 민초우(7)
group_ord = {4:1,2:1,1:1,3:2,5:2,6:2,7:3}
def group():
    boss = []
    v = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 미방문 음식을 만나면 그룹 대표 찾아서 boos[] 추가
            if v[i][j]==0:
                ti,tj = bfs(v, i, j)    # 대표자를 리턴
                food = farr[ti][tj]     # 대표자 음식 => 우선순위
                boss.append([group_ord[food], -barr[ti][tj], ti, tj])   # 전파하는 우선순위(오름차순)
    return boss

# [1] 대표자리스트(전파할 우선순위) [우선순위, -신앙심, 행, 열]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def move(blst):
    moved = set()
    for _, cn, ci, cj in blst:     # 대표자 우선순위대로 한명씩 전파 처리
        if (ci,cj) in moved:        # 당일에 이미 전파당한 경우 전파하지 않음
            continue

        cn = -cn
        di,dj = dirs[cn%4]          # 전파방향
        score = cn-1                # 간절함 초기값
        barr[ci][cj]=1              # 대표자는 1의 값을 가짐
        food = farr[ci][cj]

        while True:                 # 범위내, 간절함이 0이 아닌동안
            ci,cj = ci+di, cj+dj
            if not (0<=ci<N and 0<=cj<N) or score<=0:
                break

            if farr[ci][cj]!=food:  # 전파진행
                moved.add((ci,cj))  # 전파당함(방어상태)

                if score>barr[ci][cj]:  # 강한전파
                    farr[ci][cj]=food
                    barr[ci][cj]+=1
                    score -= barr[ci][cj]
                else:                   # 약한전파
                    farr[ci][cj]|=food  # 비트연산 or
                    barr[ci][cj]+=score
                    break               # 전파 종료

        # myprt()

def myprt():
    for lst in barr:
        print(*lst,sep='\t')
    print('-'*20)
    for lst in farr:
        print(*lst,sep='\t')
    print('='*20)

#####################################################
# [0] 입력: 민트 1<<2, 초코 1<<1, 우유 1<<0
N, T = map(int, input().split())

tbl = {'T':4, 'C':2, 'M':1}
farr = [list(input()) for _ in range(N)]
barr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        farr[i][j] = tbl[farr[i][j]]

# T일 동안 반복
for _ in range(T):
    # [1] 아침+점심: 인접(상하좌우)학생과 완전히 같을 때 그룹형성
    #    그룹대표: 신앙심 가장 큰  행이 작은  열이 작은
    #    대표자가 그룹인원수 만큼 신앙심 추가
    # [2] 그룹대표 신앙전파: 단일음식  이중조합  삼중조합
    #    같은 그룹내: 대표자의 신앙심 큰  행이 작은  열이 작은
    # [1] 대표자리스트(전파할 우선순위) [우선순위, -신앙심, 행, 열]
    blst = group()
    # myprt()

    # [2-1] 전파방법: 신앙심%4  방향(0:상, 1:하, 2:좌, 3:우) 전파
    #    간절함=신앙심-1, 간절함 0되거나 격자 밖 나가면 전파 종료
    #    같은 음식인 경우 다음 칸 이동 (다른 음식이면 전파 진행)
    #    간절함(x), 신앙심(y)인 경우
    #     1) x>y(강한전파): 동일음식 신봉(대입), x=x-(y+1), y=y+1
    #     2) x<=y(약한전파): 전파음식추가(비트), x=0, y=y+x
    #    전파 당하면(방어상태) 당일에는 전파하지 않음(전파는 받음)
    # [2] 대표자 리스트 오름차순 정렬 후 전파 진행
    blst.sort()
    move(blst)

    # 저녁 후 민초우,민초,민우,초우,우유,초코,민트순 신앙총합 출력
    # 민초우(7),민초(6),민우(5),초우(3),우유(1),초코(2),민트(4)
    # [3] 매일 저녁 이후 신앙심의 총 합을 출력
    ans = [0]*7
    for idx, food in enumerate((7,6,5,3,1,2,4)):
        for i in range(N):
            for j in range(N):
                if farr[i][j]==food:
                    ans[idx]+=barr[i][j]
    print(*ans)