N = int(input())
num = list(map(int, input().split()))

ans = 1000

def back(idx, left, right, cnt):
    global ans

    if cnt == len(num) // 2:
        ans = min(ans, abs(left - right))
        return
    
    for i in range(idx, len(num)):
        back(i + 1, left + num[i], right - num[i], cnt + 1)

back(0, 0, sum(num), 0)
print(ans)