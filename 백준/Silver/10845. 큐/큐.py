import sys

N = int(input())

queue = []

def push(num):
    queue.append(num)

def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.pop(0)

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

for _ in range(N):
    command = sys.stdin.readline().strip()
    
    if command[:4] == 'push':
        command, num = command.split()
        push(num)
    elif command == 'pop':
        pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'front':
        front()
    else:
        back()
