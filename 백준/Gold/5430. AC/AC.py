import sys
T = int(input())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(input())
    li = sys.stdin.readline().strip()
    num = li[1:-1]
    flag = 0
    rev = 0
    
    if ',' in num:
        num = num.split(',')
    else:
        num = [num]
        
    for i in p:
        if i == 'R':
            rev += 1
        else:
            if len(num) == 0 or num == ['']:
                flag = 1
                break
            else:
                if rev % 2 == 0:
                    num.pop(0)
                else:
                    num.pop()
    
    if flag == 1:
        print('error')
    else:
        if len(num) == (0 or 1):
            res = ''.join(num)
            print('[' + res + ']')
        elif rev % 2 != 0:
            num.reverse()
            res = ','.join(num)
            print('[' + res + ']')
        else:
            res = ','.join(num)
            print('[' + res + ']')