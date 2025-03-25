N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

add_max = 0

for i in range(1, N):
    for j in range(1, M):
        # ㄴ 모양
        add1 = grid[i - 1][j - 1] + grid[i][j - 1] + grid[i][j]
        # ㄱ 반대 모양
        add2 = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i][j - 1]
        # ㄱ 모양
        add3 = grid[i - 1][j - 1] + grid[i - 1][j] + grid[i][j]
        # ㄴ 반대 모양
        add4 = grid[i - 1][j] + grid[i][j - 1] + grid[i][j]
        
        add_max = max(add1, add2, add3, add4, add_max)

for i in range(N):
    # ㅡ 모양
    for j in range(2, M):
        add5 = grid[i][j - 2] + grid[i][j - 1] + grid[i][j]
        add_max = max(add5, add_max)

for i in range(2, N):
    # l 모양
    for j in range(M):
        add6 = grid[i - 2][j] + grid[i - 1][j] + grid[i][j]
        add_max = max(add6, add_max)

print(add_max)