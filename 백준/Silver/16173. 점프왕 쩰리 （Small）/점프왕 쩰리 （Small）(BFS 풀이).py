from collections import deque

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

def bfs():
    queue = deque([(0, 0)])
    
    visit = [[0] * N for _ in range(N)]
    visit[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        # 목표 지점에 도달한다면
        if graph[x][y] == -1:
            return True
        
        step = graph[x][y]
        
        # 아래로 이동
        if x + step < N and visit[x + step][y] != 1:
            visit[x + step][y] = 1
            queue.append((x + step, y))

        # 오른쪽으로 이동
        if y + step < N and visit[x][y + step] != 1:
            visit[x][y + step] = 1
            queue.append((x, y + step))
    
    # 목표 지점에 도달하지 못한다면
    return False

if bfs():
    print('HaruHaru')
else:
    print('Hing')