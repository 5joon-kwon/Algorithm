import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (3) for _ in range(n)]

# 처음 집: R or G or B
dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

for i in range(1, n):
    # i번째 집이 R일 때
    dp[i][0] = min(cost[i][0] + dp[i - 1][1], cost[i][0] + dp[i - 1][2])
    # i번째 집이 G일 때
    dp[i][1] = min(cost[i][1] + dp[i - 1][0], cost[i][1] + dp[i - 1][2])
    # i번째 집이 B일 때
    dp[i][2] = min(cost[i][2] + dp[i - 1][0], cost[i][2] + dp[i - 1][1])

print(min(dp[n - 1]))