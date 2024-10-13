import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    num_li = []
    for _ in range(n):
        # 목록을 미리 다 받기
        num_li.append(input().strip())
        
    # 받은 목록을 사전순으로 오름차순 정렬
    num_li.sort()
    flag = False
    
    # 이웃한 두 번호를 비교
    for i in range(len(num_li) - 1):
        if num_li[i] == num_li[i+1][:len(num_li[i])]:
            flag = True
            break
    
    if flag:
        print('NO')
    else:
        print('YES')