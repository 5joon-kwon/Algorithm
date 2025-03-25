N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

res = 0

for i in range(N):
    cnt = 1

    if N == 1 and M == 1:
        res += 1
        break

    if N == 1 and M != 1:
        break

    for j in range(0, N - 1):
        if grid[i][j] == grid[i][j + 1]:
            cnt += 1
        else:
            cnt = 1

        if cnt >= M:
            res += 1
            break        
        
for j in range(N):
    cnt = 1

    if N == 1 and M == 1:
        res += 1
        break

    if N == 1 and M != 1:
        break

    for i in range(0, N - 1):
        if grid[i][j] == grid[i + 1][j]:
            cnt += 1
        else:
            cnt = 1
    
        if cnt >= M:
            res += 1
            break
        
print(res)
