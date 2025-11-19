from collections import deque

n, m = map(int, input().split())
i, j, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque([[i, j, d]])
cnt = 0

while q:
    si, sj, sd = q.popleft()
    
    # 현재 칸 청소 X
    if grid[si][sj] == 0:
        cnt += 1
        grid[si][sj] = 2 # 청소 완료
    
    # 주변 4칸
    flag = False    # 청소 안된 칸 있는지
    for dr in range(4):
        ni, nj = si + dx[dr], sj + dy[dr]
        
        if 0 > ni or ni >= n or 0 > nj or nj >= m:
            continue
        
        # 청소 X
        if grid[ni][nj] == 0:
            flag = True     # 청소 안된 칸 존재
            break
    
    # 청소 안된 칸 있으면
    if flag:
        for _ in range(4):
            sd = (sd - 1) % 4   # 반시계 90도 회전
            ri, rj = si + dx[sd], sj + dy[sd]   # 회전 방향 앞칸
            # 바라보는 방향으로 앞쪽 칸이 청소 안한 칸이면 전진
            if 0 <= ri < n and 0 <= rj < m and grid[ri][rj] == 0:
                q.append([ri, rj, sd])
                break
    # 없으면
    else:
        bd = (sd - 2) % 4   # 후진
        bi, bj = si + dx[bd], sj + dy[bd]
        if 0 > bi or bi >= n or 0 > bj or bj >= m or grid[bi][bj] == 1:
            break
        q.append([bi, bj, sd])

print(cnt)