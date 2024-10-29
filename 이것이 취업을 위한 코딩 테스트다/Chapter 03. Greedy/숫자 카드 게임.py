N, M = map(int, input().split())

res = 0

for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    res = max(res, min_value)

print(res)