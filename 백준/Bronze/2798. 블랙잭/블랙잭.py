N, M = map(int, input().split())

card = list(map(int, input().split()))

max_value = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            res = card[i] + card[j] + card[k]
            if res <= M:
                max_value = max(max_value, res)

print(max_value)