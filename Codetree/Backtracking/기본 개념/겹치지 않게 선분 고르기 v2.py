N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

ans = 0
pick = []

def back(idx, cur_cnt, end):
    global ans
    
    if idx == N:
        ans = max(ans, cur_cnt)
        return
    
    s, e = lines[idx]

    if end < s:
        pick.append([s, e])
        back(idx + 1, cur_cnt + 1, e)
        pick.pop()
    
    back(idx + 1, cur_cnt, end)

back(0, 0, -1)
print(ans)