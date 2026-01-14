N, M = map(int, input().split())

ans = []

def back(idx):
    if len(ans) == M:
        print(*ans)
        return
    
    for i in range(idx, N + 1):
        ans.append(i)
        back(i + 1)
        ans.pop()

back(1)