n, m = map(int, input().split())
i, j, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0

while True:  
    # 현재 칸 청소 X
    if grid[i][j] == 0:
        cnt += 1
        grid[i][j] = 2 # 청소 완료
    
    flag = False   # 회전 후 청소하러 이동했는지 

    for _ in range(4):
        d = (d - 1) % 4   # 반시계 90도 회전
        ri, rj = i + dx[d], j + dy[d]   # 회전 방향 앞칸
        # 바라보는 방향으로 앞쪽 칸이 청소 안한 칸이면 전진
        if 0 <= ri < n and 0 <= rj < m and grid[ri][rj] == 0:
            i, j = ri, rj
            flag = True
            break
    
    # 회전 후 청소하러 이동했으면
    if flag:
        continue
    
    # 이동 못했으면
    bd = (d - 2) % 4   # 후진
    bi, bj = i + dx[bd], j + dy[bd]
    
    if 0 > bi or bi >= n or 0 > bj or bj >= m or grid[bi][bj] == 1:
        break
    
    i, j = bi, bj

print(cnt)