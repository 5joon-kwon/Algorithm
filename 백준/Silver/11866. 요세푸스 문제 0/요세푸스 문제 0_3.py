N, K = map(int, input().split())

num_list = [i for i in range(1, N + 1)]
start = 0
res = []

while num_list:
    start += K - 1
    # 나머지 연산으로 리스트의 인덱스 순환
    start %= len(num_list)
    res.append(num_list.pop(start))

print('<', end='')
print(', '.join(f'{i}' for i in res), end='')
print('>')