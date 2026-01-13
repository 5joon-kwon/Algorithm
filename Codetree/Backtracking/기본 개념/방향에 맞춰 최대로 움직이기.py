n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
dirs = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

di = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 0, 1, 1, 1, 0, -1, -1, -1]

ans = 0

def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def back(i, j, cnt):
    global ans

    d = dirs[i][j]
    moved = False

    k = 1
    while True:
        ni, nj = i + di[d] * k, j + dj[d] * k
        if not in_range(ni, nj):
            break

        if nums[ni][nj] > nums[i][j]:
            moved = True
            back(ni, nj, cnt + 1)

        k += 1

    if not moved:
        ans = max(ans, cnt)

back(r - 1, c - 1, 0)
print(ans)
