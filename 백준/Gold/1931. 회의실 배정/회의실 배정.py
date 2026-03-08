import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key = lambda x: (x[1], x[0]))

res = []
for s, e in time:
    if len(res) == 0:
        res.append((s, e))
        continue

    if s >= res[-1][1]:
        res.append((s, e))

print(len(res))