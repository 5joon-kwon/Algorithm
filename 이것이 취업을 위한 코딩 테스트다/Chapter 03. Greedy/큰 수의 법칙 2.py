N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

# 만약 가장 큰 수가 2개 이상이라면 index가 서로 다르므로 두 수를 번갈아 K 번씩 더하면 된다.
# 그게 아니라면 서로 다른 수를 K 번씩 더하면 된다.
first = data[N - 1]
second = data[N - 2]

# K 번 이하로 반복돼야 하므로, 그 다음 큰 수까지 더한 K + 1 번의 수열이 반복되어 더해지는 패턴
# K + 1 번의 수열이 M 동안 몇번 반복되는지 구하는 식 : M // (K + 1)
# M // K + 1 의 결과가 x 이면,
# 가장 큰 수가 K 번 더해지는 과정이 x 번 반복되는 것이다.
count = K * (M // (K + 1))

# 만약 M // (K + 1) 의 결과에서 나머지 y 가 발생했다면, 가장 큰 수가 추가로 y 번 더해지면 된다.
count += M % (K + 1)

result = 0

# 즉, count 는 가장 큰 수가 몇번 더해지면 되는지를 알려준다.
result += count * first

# 두 번째로 큰 수는, 전체 반복 횟수 M - count 를 하면 된다.
result += (M - count) * second

print(result)