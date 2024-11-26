from collections import deque

dq = deque()

dq.append(5)
dq.append(2)
dq.append(3)
dq.append(7)
dq.popleft()
dq.append(1)
dq.append(4)
dq.popleft()

print(dq)