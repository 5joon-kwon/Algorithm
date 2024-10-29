N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# 만약 가장 큰 수가 2개 이상이라면, 큰 수끼리는 index가 서로 다르므로 두 수를 번갈아 K 번씩 더하면 된다.
# 그게 아니라면 서로 다른 수를 K 번씩 더하면 된다.
first = data[N - 1]
second = data[N - 2]

result = 0

while True:
    # 가장 큰 수는 K 번 더해주기
    for i in range(K):
        if M == 0:
            break
        result += first
        M -= 1
    if M == 0:
        break
    # 두 번째로 큰 수(가장 큰 수 일 수도 있음)는 1번 더해주기
    result += second
    M -= 1

print(result)
