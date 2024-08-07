from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    totq1 = sum(q1)
    totq2 = sum(q2)
    tot = totq1 + totq2
    
    count = 0
    while totq1 != tot//2: # queue1만 생각하자
        if totq1 < tot//2: # queue1 원소의 합 < tot // 2
            num = q2.popleft()
            q1.append(num)
            totq1 += num
        else:              # queue1 원소의 합 > tot // 2
            num = q1.popleft()
            totq1 -= num 
        count += 1
        if not q2: # queue2에서는 pop만 진행. queue1 원소합만 생각하면 되기 때문
            count = -1
            break
    return count