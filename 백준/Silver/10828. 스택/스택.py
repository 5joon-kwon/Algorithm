import sys
from collections import deque

N = int(input())
stack = deque()

for _ in range(N):
    order = sys.stdin.readline().strip()
    if order[:4] == 'push':
        order, x = order.split()
        stack.append(x)
    elif order == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)
    elif order == 'size':
        print(len(stack))
    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])