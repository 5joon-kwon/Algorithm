import sys

N = int(sys.stdin.readline())
list_N = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
list_M = list(map(int, sys.stdin.readline().split()))

sorted_N = sorted(list_N)

for i in list_M:
    left, right = 0, len(sorted_N) - 1
    flag = 0
    
    while left <= right:
        mid = (left + right) // 2
        
        if i == sorted_N[mid]:
            flag = 1
            break
        elif i < sorted_N[mid]:
            right = mid - 1
        else:
            left = mid + 1
                
    if flag == 1:
        print(1)
    else:
        print(0)