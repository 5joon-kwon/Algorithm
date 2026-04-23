n = int(input())
grid = [[0] * 1002 for _ in range(1002)]

idx = 1
for _ in range(n):
    lx, ly, w, h = map(int, input().split())
    for y in range(ly, ly + h):
        for x in range(lx, lx + w):
            grid[y][x] = idx
    idx += 1

ans = [0] * (n + 1)
for i in range(1002):
    for j in range(1002):
        if grid[i][j] != 0:
            ans[grid[i][j]] += 1

for i in ans[1:]:
    print(i)