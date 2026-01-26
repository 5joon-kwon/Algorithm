N = int(input())
durability = []
weight = []

for _ in range(N):
    d, w = map(int, input().split())
    durability.append(d)
    weight.append(w)

ans = 0

# 깨진 계란 세기
def cnt():
    count = 0
    for d in durability:
        if d <= 0:
            count += 1
    
    return count

def back(idx):
    global ans

    # 맨 오른쪽 계란
    if idx == N:
        ans = max(ans, cnt())
        return

    # 현재 손에 든 계란이 깨졌다면
    if durability[idx] <= 0:
        # 다음 계란으로 이동
        back(idx + 1)
        return
    
    # 칠 수 있는 계란 있는지 파악하기 위함
    can_hit = False

    for i in range(N):
        # 자기 자신 제외 + 깨진 계란 제외
        if i == idx or durability[i] <= 0:
            continue
        
        # 칠 수 있는 계란이라면
        can_hit = True

        durability[idx] -= weight[i]
        durability[i] -= weight[idx]

        back(idx + 1)

        durability[idx] += weight[i]
        durability[i] += weight[idx]
    
    # 모든 계란이 깨져있다면
    if not can_hit:
        back(idx + 1)

back(0)
print(ans)