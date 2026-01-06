def beauty():
    global cnt

    if len(ans) == n:
        cnt += 1
        return

    for i in range(1, 5):
        if len(ans) + i > n:
            return
        
        ans.extend([i] * i)
        beauty()
        for j in range(i):
            ans.pop()

n = int(input())
ans = []
cnt = 0

beauty()
print(cnt)