from collections import deque

N, M = map(int, input().split())

grid = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

q = deque([[0, 0, 0]])
visited[0][0][0] = 1

ans = -1

while q:
    si, sj, flag = q.popleft()
    if si == N - 1 and sj == M - 1:
        ans = visited[si][sj][flag]
        break
    
    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        
        if 0 <= ni < N and 0 <= nj < M:
            if grid[ni][nj] != 1 and visited[ni][nj][flag] == 0:
                visited[ni][nj][flag] = visited[si][sj][flag] + 1
                q.append([ni, nj, flag])
            elif grid[ni][nj] == 1 and flag == 0 and visited[ni][nj][1] == 0:
                visited[ni][nj][1] = visited[si][sj][0] + 1
                q.append([ni, nj, 1])

print(ans)