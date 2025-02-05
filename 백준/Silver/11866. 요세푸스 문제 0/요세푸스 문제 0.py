N, K = map(int, input().split())

num_list = [i for i in range(1, N + 1)]
start = 0
res = []

while len(num_list) != 0:
    order = start + K - 1
    while order >= len(num_list):
            order -= len(num_list)
    res.append(num_list.pop(order))
    start = order

print('<', end='')
print(', '.join(f'{i}' for i in res), end='')
print('>')
