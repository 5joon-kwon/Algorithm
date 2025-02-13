from collections import deque
import sys

input = sys.stdin.readline

K = int(input())
queue = deque()
tot = 0

for _ in range(K):
    num = int(input())
    if num == 0:
        tot -= queue.pop()
    else:
        tot += num
        queue.append(num)

print(tot)