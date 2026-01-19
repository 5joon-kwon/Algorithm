N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

j_set = []
ans = 0

def back(i, cur):
    global ans
    
    if i == N:
        ans = max(ans, cur)
        return
    
    for j in range(N):
        if j in j_set:
            continue

        j_set.append(j)
        back(i + 1, cur + grid[i][j])
        j_set.pop()

back(0, 0)
print(ans)
