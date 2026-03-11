import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = []
L = []
R = []

for _ in range(n):
    a, b = map(int, input().split())
    l = a - b
    r = a + b
    arr.append((l, r))
    L.append(l)
    R.append(r)

L.sort()
R.sort()

for l, r in arr:
    # 최소 순위:
    # 나보다 무조건 앞에 오는 원소 개수 = R_j < l 인 원소 수
    min_rank = bisect_left(R, l) + 1

    # 최대 순위:
    # 나보다 앞에 올 수 있는 원소 개수 = L_j <= r 인 원소 수
    max_rank = bisect_right(L, r)

    print(min_rank, max_rank)