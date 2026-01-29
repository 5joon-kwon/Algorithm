N = int(input())
scores = [0] + [int(input()) for _ in range(N)]

dp_table = [0] * (N + 1)

if N >= 1:
    dp_table[1] = dp_table[0] + scores[1]

if N >= 2:
    dp_table[2] = max(dp_table[1] + scores[2], dp_table[0] + scores[2])

for i in range(3, N + 1):
    dp_table[i] = max(dp_table[i - 2] + scores[i], dp_table[i - 3] + scores[i - 1] + scores[i])

print(dp_table[-1])