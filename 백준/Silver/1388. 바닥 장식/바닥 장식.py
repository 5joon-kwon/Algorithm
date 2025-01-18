N, M = map(int, input().split())

def dfs(x, y):
    if wood[x][y] == '-':
        wood[x][y] = 1
        for dy in [1, -1]:
            beside_y = y + dy
            if 0 <= beside_y < M and wood[x][beside_y] == '-':
                dfs(x, beside_y)
    
    if wood[x][y] == '|':
        wood[x][y] = 1
        for dx in [1, -1]:
            beside_x = x + dx
            if 0 <= beside_x < N and wood[beside_x][y] == '|':
                dfs(beside_x, y)

wood = [list(input()) for _ in range(N)]
count = 0

for i in range(N):
    for j in range(M):
        if wood[i][j] in ('-', '|'):
            dfs(i, j)
            count += 1

print(count)