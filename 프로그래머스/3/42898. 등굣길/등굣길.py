def solution(m, n, puddles):
    # 시작 (1, 1) 종료 (m, n)
    # 장애물: puddles
    grid = [[0] * m for _ in range(n)]
    pud = []
    for i, j in puddles:
        pud.append([j - 1, i - 1])
    
    grid[0][0] = 1
    for i in range(n):
        for j in range(m):
            
            if (i, j) == (0, 0):
                continue
            
            if [i, j] in pud:
                continue
            
            if i == 0:
                if grid[i][j - 1] == 0:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1
                continue
            
            if j == 0:
                if grid[i - 1][j] == 0:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1
                continue
            
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
            
    answer = grid[n - 1][m - 1] % 1000000007
    return answer