N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
li = []

def move(comb):
    score = 0
    horse = [1] * (K + 1)

    for i in range(N):
        if horse[comb[i]] == M:
            continue

        if horse[comb[i]] + nums[i] >= M:
            horse[comb[i]] = M
            score += 1
        else:
            horse[comb[i]] += nums[i]
            
    return score

def back():
    global li, ans

    if len(li) == N:
        ans = max(ans, move(li))
        return

    for i in range(1, K + 1):
        li.append(i)
        back()
        li.pop()

back()
print(ans)