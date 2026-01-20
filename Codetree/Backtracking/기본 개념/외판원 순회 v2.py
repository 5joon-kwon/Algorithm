N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

ans = float('inf')
v = [True] + [False] * (N - 1)

# curr: 현재 도시, cnt: 방문한 도시 수, cost: 누적 비용
def back(curr, cnt, cost):
    global ans
    
    if cost >= ans:
      return

    if cnt == N:
      if A[curr][0] > 0:
        ans = min(ans, cost + A[curr][0])
      return

    for next in range(1, N):
        if v[next] or A[curr][next] == 0:
            continue
        
        v[next] = True
        back(next, cnt + 1, cost + A[curr][next])
        v[next] = False
    
back(0, 1, 0)
print(ans)