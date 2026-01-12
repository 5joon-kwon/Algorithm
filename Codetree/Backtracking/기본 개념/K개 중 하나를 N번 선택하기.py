K, N = map(int, input().split())
ans = []

def back():
    if len(ans) == N:
        for i in ans:
            print(i, end=' ')
        print()
        return
    
    for i in range(1, K + 1):
        if len(ans) >= 2 and ans[-2] == ans[-1] == i:
            continue
        
        ans.append(i)
        back()
        ans.pop()

back()