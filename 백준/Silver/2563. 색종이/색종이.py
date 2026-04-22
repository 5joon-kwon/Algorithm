n = int(input())
grid = [[0] * 101 for _ in range(101)]

for _ in range(n):
    lx, ly = map(int, input().split())
    ly = 100 - ly

    for i in range(ly - 10, ly):
        for j in range(lx, lx + 10):
            grid[i][j] = 1
    
count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1:
            count += 1

print(count)