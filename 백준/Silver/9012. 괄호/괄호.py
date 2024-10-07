import sys

T = int(input())

for _ in range(T):
    left = []
    flag = 0
    S = sys.stdin.readline().strip()
    
    for i in S:
        if i == '(':
            left.append(i)
        else:
            if len(left) != 0:
                left.pop()
            elif len(left) == 0:
                print('NO')
                flag = 1
                break

    if len(left) == 0 and flag == 0:
        print('YES')
    elif len(left) != 0 and flag == 0:
        print('NO')