N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')

li = [0]
v = [True] + [False] * (N - 1)

def back():
    global ans

    if len(li) == N:
        cnt = 0
        li.append(0)

        for i in range(len(li) - 1):
            if A[li[i]][li[i + 1]] == 0:
                li.pop()
                return

            cnt += A[li[i]][li[i + 1]]
        ans = min(ans, cnt)
        li.pop()
        return

    for i in range(1, N):
        if v[i]:
            continue
        
        v[i] = True
        li.append(i)
        back()
        li.pop()
        v[i] = False
    
back()
print(ans)