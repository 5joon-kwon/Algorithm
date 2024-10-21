import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    S = input().strip()
    front = 0
    back = len(S) - 1
    flag = 0
    
    while front < back:
        if S[front] == S[back]:
            front += 1
            back -= 1
        else:
            del_front = S[:front] + S[front+1:]
            del_back = S[:back] + S[back+1:]
            if del_front == del_front[::-1] or del_back == del_back[::-1]:
                    flag = 1
                    break
            else:
                flag = 2
                break
            
    if flag == 0:
        print('0')
    elif flag == 1:
        print('1')
    else:
        print('2')