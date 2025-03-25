N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max = 0

for i in range(0, len(grid[0]) - 2):
    for j in range(0, N - 2):
        cnt = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
        if max < cnt:
            max = cnt 
            
print(max)
