import sys
from collections import deque

# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

def find_balls():
    ri, rj, bi, bj = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                ri, rj = i, j
            elif board[i][j] == 'B':
                bi, bj = i, j
    
    return ri, rj, bi, bj

def move(i, j, di, dj):
    dist = 0
    while True:
        if board[i][j] == 'O':
            break

        if board[i + di][j + dj] == '#':
            break
        
        i += di
        j += dj
        dist += 1

    return i, j, dist

def bfs(ri, rj, bi, bj):
    q = deque([(ri, rj, bi, bj, 0)])
    v = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    v[ri][rj][bi][bj] = 1

    while q:
        sri, srj, sbi, sbj, cnt = q.popleft()

        if cnt >= 10:
            continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nri, nrj, rdist = move(sri, srj, di, dj)
            nbi, nbj, bdist = move(sbi, sbj, di, dj)

            # 파랑 구슬은 구멍에 들어가면 안됨
            if board[nbi][nbj] == 'O':
                continue
            
            # 빨강 구슬이 구멍에 들어감
            if board[nri][nrj] == 'O':
                return cnt + 1
            
            # 빨, 파는 동시에 같은 칸 x
            if nri == nbi and nrj == nbj:
                # 빨강이 더 많이 이동한 경우
                if rdist > bdist:
                    nri -= di
                    nrj -= dj
                else:
                    nbi -= di
                    nbj -= dj
            
            if v[nri][nrj][nbi][nbj] == 0:
                q.append((nri, nrj, nbi, nbj, cnt + 1))
                v[nri][nrj][nbi][nbj] = 1
    
    return -1

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]
ri, rj, bi, bj= find_balls()
print(bfs(ri, rj, bi, bj))
