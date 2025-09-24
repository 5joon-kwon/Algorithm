from collections import deque

def bfs(si, sj):
    q = deque()
    visited = [[0] * (C + 2) for _ in range(R + 4)]
    
    q.append((si, sj))
    visited[si][sj] = 1
    max_i = 0
    
    while q:
        ci, cj = q.popleft()
        max_i = max(max_i, ci)
        
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if visited[ni][nj] == 0 and (arr[ci][cj] == arr[ni][nj] or ((ci, cj) in exit_set and arr[ni][nj] > 0)):
                q.append((ni, nj))
                visited[ni][nj] = 1
    
    return max_i - 2

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

R, C, K = map(int, input().split())
golem = [list(map(int, input().split())) for _ in range(K)]

arr = [[-1] + [0] * C + [-1] for _ in range(R + 3)]+ [[-1] * (C + 2)]
exit_set = set()

ans = 0
num = 1
for gj, gd in golem:
    gi = 1
    
    while True:
        if arr[gi + 1][gj - 1] == 0 and arr[gi + 1][gj + 1] == 0 and arr[gi + 2][gj] == 0:
            gi += 1
        elif arr[gi - 1][gj - 1] == 0 and arr[gi + 1][gj - 1] == 0 and arr[gi][gj - 2] == 0 and arr[gi + 2][gj - 1] == 0 and arr[gi + 1][gj - 2] == 0:
            gi += 1
            gj -= 1
            gd = (gd - 1) % 4
        elif arr[gi - 1][gj + 1] == 0 and arr[gi + 1][gj + 1] == 0 and arr[gi][gj + 2] == 0 and arr[gi + 2][gj + 1] == 0 and arr[gi + 1][gj + 2] == 0:
            gi += 1
            gj += 1
            gd = (gd + 1) % 4
        else:
            break
    
    if gi < 4:
        arr = [[-1] + [0] * C + [-1] for _ in range(R + 3)]+ [[-1] * (C + 2)]
        num = 1
        exit_set = set()
    else:
        arr[gi][gj] = arr[gi - 1][gj] = arr[gi + 1][gj] =arr[gi][gj - 1] = arr[gi][gj + 1] = num
        num += 1
        exit_set.add((gi + di[gd], gj + dj[gd]))

        ans += bfs(gi, gj)
        
print(ans)