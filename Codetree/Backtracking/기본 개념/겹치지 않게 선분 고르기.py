N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

ans = 0
li = []

def back(idx, cur_cnt, start, end):
    global ans
    
    if idx == N:
        ans = max(ans, cur_cnt)
        return
    
    for i in range(idx, N):
        s, e = lines[idx]

        if start == s:
            li.pop()
            li.append([s, e])
            back(i + 1, cur_cnt, s, e)

        if end < s:
            li.append([s, e])
            back(i + 1, cur_cnt + 1, s, e)
            li.pop()

        back(i + 1, cur_cnt, start, end)

back(0, 0, -1, -1)
print(ans)