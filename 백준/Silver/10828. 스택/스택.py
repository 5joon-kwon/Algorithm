import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    order = input().strip()

    if order == 'pop':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
            li.pop()
    elif order == 'size':
        print(len(li))
    elif order == 'empty':
        if len(li) == 0:
            print(1)
        else:
            print(0)
    elif order == 'top':
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
    else:
        o, num = order.split()
        li.append(num)
