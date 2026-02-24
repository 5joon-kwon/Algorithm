import sys
input = sys.stdin.readline

n = int(input())
drinks = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(drinks[1])
elif n == 2:
    print(drinks[1] + drinks[2])
else:
    dp = [0] * (n + 1)
    dp[1] = drinks[1]
    dp[2] = drinks[1] + drinks[2]
    
    for i in range(3, n + 1):
        # i 번째 안마심: dp[i - 1]
        # i 번째 마심
        # 1. i - 1 번째 안마심: dp[i - 2] + drinks[i]
        # 2. i - 1 번째 마심: dp[i - 3] + drinks[i - 1] + drinks[i]
        #    dp[i - 1] 이 아닌 이유: i - 2를 마셨을 수도 있음
        dp[i] = max(dp[i - 1], dp[i - 2] + drinks[i], dp[i - 3] + drinks[i - 1] + drinks[i])
    print(dp[-1])
