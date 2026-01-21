N = int(input())
dur = []
wt = []
for _ in range(N):
    d, w = map(int, input().split())
    dur.append(d)
    wt.append(w)

ans = 0

def back(idx):
    global ans

    if idx == N:
        ans = max(ans, sum(1 for x in dur if x <= 0))
        return

    # 현재 손에 든 계란이 이미 깨졌으면 다음으로
    if dur[idx] <= 0:
        back(idx + 1)
        return

    hit = False
    for j in range(N):
        if j == idx or dur[j] <= 0:
            continue

        hit = True
        # 때리기
        dur[idx] -= wt[j]
        dur[j] -= wt[idx]

        back(idx + 1)

        # 복구
        dur[idx] += wt[j]
        dur[j] += wt[idx]

    # 칠 수 있는 계란이 없으면 그냥 넘어감
    if not hit:
        back(idx + 1)

back(0)
print(ans)