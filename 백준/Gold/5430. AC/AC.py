import sys
T = int(input())

for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(input())
    li = sys.stdin.readline().strip()
    num = li[1:-1]
    flag = 0
    # Reverse에 대한 flag를 하나 만들었다.
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
                # R이 짝수번 나왔다면 list에서 처음 요소를 제거한다.
                if rev % 2 == 0:
                    num.pop(0)
                # # R이 홀수번 나왔다면 list에서 마지막 요소를 제거한다.
                else:
                    num.pop()
    
    if flag == 1:
        print('error')
    else:
        if len(num) == (0 or 1):
            res = ''.join(num)
            print('[' + res + ']')
        elif rev % 2 != 0:
            # R이 홀수번 나왔다면 list의 요소를 뒤집어 준다.
            # 최종적으로 한번만 list를 뒤집어 주면 된다 !
            num.reverse()
            res = ','.join(num)
            print('[' + res + ']')
        else:
            res = ','.join(num)
            print('[' + res + ']')
