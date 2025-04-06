n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

tet = [
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], # ㅣ
    [(0, 1), (1, 0), (1, 1)], # ㅁ
    [(1, 0), (1, 1), (2, 1)], [(0, 1), (1, 1), (1, 2)], [(0, 1), (-1, 1), (-1, 2)], [(1, 0), (0, 1), (-1, 1)], # Harry
    [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (-1, 2)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (0, 1), (0, 2)], # L
    [(0, 1), (1, 0), (2, 0)], [(0, 1), (0, 2), (1, 2)], [(0, 1), (-1, 1), (-2, 1)], [(1, 0), (1, 1), (1, 2)], # L 반전
    [(1, 0), (1, 1), (2, 0)], [(1, 0), (1, -1), (1, 1)], [(0, 1), (-1, 1), (1, 1)], [(0, 1), (0, 2), (1, 1)] # ㅏㅏ
    ]

ans = 0

def test(i, j, shape):
    s = grid[i][j]
    for dx, dy in shape:
        nx, ny = i + dx, j + dy
        if 0 <= nx < n and 0 <= ny < m:
            s += grid[nx][ny]
        else:
            return 0
    return s


for i in range(n):
    for j in range(m):
        for shape in tet:
            v = test(i, j, shape)
            ans = max(ans, v)

print(ans)