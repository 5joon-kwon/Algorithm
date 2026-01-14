N, M = map(int, input().split())
A = list(map(int, input().split()))

ans = 0

def back(idx, cur, cnt):
    global ans

    if cnt == M:
        ans = max(ans, cur)
        return
    
    for i in range(idx, N):
        back(i + 1, cur ^ A[i], cnt + 1)

back(0, 0, 0)
print(ans)