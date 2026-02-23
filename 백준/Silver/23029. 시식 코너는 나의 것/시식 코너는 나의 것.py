import sys
input = sys.stdin.readline

N = int(input())
foods = [0]
for _ in range(N):
    foods.append(int(input()))

# n차원 DP
# 미래 결정을 위해 반드시 기억해야 하는 정보의 개수 = 상태 차원 수

# dp[i][0]: i 번째에서 모두 먹음
# dp[i][1]: i 번째에서 절반 먹음
# dp[i][2]: i 번째에서 안 먹음
dp = [[0] * 3 for _ in range(N + 1)]

dp[1][0] = foods[1]
dp[1][1] = foods[1] // 2
dp[1][2] = 0

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][2] + foods[i]
    dp[i][1] = dp[i - 1][0] + foods[i] // 2
    # 안 먹을 때: i - 1 까지의 최대 상태값
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

print(max(dp[N]))