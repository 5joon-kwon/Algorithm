from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))
    
    flag = deque('0' * N)
    flag[M] = '1'
    
    maxi = max(queue)
    cnt = 1
    want = queue[M]
    
    while True:
        if queue[0] == want and queue[0] == maxi and flag[0] == '1':
            print(cnt)
            break
        
        if queue[0] != maxi:
            a = queue.popleft()
            queue.append(a)
            b = flag.popleft()
            flag.append(b)
        else:
            queue.popleft()
            flag.popleft()
            cnt += 1
            maxi = max(queue)
            