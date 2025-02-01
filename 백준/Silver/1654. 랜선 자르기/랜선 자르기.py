import sys

K, N = map(int, input().split())
line = [int(sys.stdin.readline()) for _ in range(K)]

left, right = 1, max(line)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(l // mid for l in line)
    
    if count >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)