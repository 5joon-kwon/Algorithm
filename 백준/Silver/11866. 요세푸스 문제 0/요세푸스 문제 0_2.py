from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1))

res = []

while queue:
    # deque에서 K - 1 개의 요소를 앞에서 뒤로 (-) 보냄 !
    queue.rotate(-(K - 1))
    res.append(queue.popleft())

print('<', end='')
print(', '.join(f'{i}' for i in res), end='')
print('>')