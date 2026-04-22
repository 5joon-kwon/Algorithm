import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    li = list(input().rstrip())
    ans = []
    flag = False
    
    for i in li:
        if i == '(':
            ans.append(i)
        else:
            if len(ans) == 0:
                print('NO')
                flag = True
                break
            ans.pop()
    
    if flag:
        continue

    if len(ans) == 0:
        print('YES')
    else:
        print('NO')
