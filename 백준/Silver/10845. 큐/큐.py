import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

from collections import deque

n = int(input())
li = deque()
for _ in range(n):
    order = input().rstrip()

    if order == 'pop':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
            li.popleft()
    elif order == 'size':
        print(len(li))
    elif order == 'empty':
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if len(li) == 0:
            print(-1)
        else:
            print(li[0])
    elif order == 'back':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
    else:
        o, num = order.split()
        li.append(num)
