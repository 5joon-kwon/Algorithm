import sys
from collections import deque

input = sys.stdin.readline

def move(x, y, dx, dy):
    cnt = 0
    # 다음 칸이 벽이 아니고, 현재 칸이 구멍이 아닐 때 계속 이동
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
        if board[x][y] == 'O':
            break
    return x, y, cnt

def bfs():
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited[rx][ry][bx][by] = True

    while q:
        crx, cry, cbx, cby, depth = q.popleft()

        # 10번까지만 허용
        if depth >= 10:
            continue

        for dx, dy in directions:
            nrx, nry, rcnt = move(crx, cry, dx, dy)
            nbx, nby, bcnt = move(cbx, cby, dx, dy)

            # 파란 구슬이 구멍에 빠지면 실패
            if board[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 구멍에 빠지면 성공
            if board[nrx][nry] == 'O':
                return depth + 1

            # 두 구슬이 같은 위치에 멈췄다면 조정
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1


n, m = map(int, input().split())
board = []
rx = ry = bx = by = 0

for i in range(n):
    row = list(input().strip())
    for j in range(m):
        if row[j] == 'R':
            rx, ry = i, j
            row[j] = '.'
        elif row[j] == 'B':
            bx, by = i, j
            row[j] = '.'
    board.append(row)

visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

print(bfs())