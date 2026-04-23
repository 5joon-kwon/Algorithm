n, m = map(int, input().split())
i, j, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
count = 0

def in_range(i, j):
    return 0 <= i < n and 0 <= j < m
    
# 북, 동, 남, 서
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

while True:
    clean_possible = False

    # 청소해야하는 칸
    if grid[i][j] == 0:
        count += 1
        grid[i][j] = 2
    
    # 주변 4칸 확인
    for _ in range(4):
        d = (d + 3) % 4
        ni, nj = i + di[d], j + dj[d]
        if in_range(ni, nj) and grid[ni][nj] == 0:
            clean_possible = True
            i, j = ni, nj
            break
    
    if not clean_possible:
        ni, nj = i - di[d], j - dj[d]

        if in_range(ni, nj):
            if grid[ni][nj] == 1:
                break
            else:
                i, j = ni, nj

print(count)