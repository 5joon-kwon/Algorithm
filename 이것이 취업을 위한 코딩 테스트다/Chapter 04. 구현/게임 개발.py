N, M = map(int, input().split())
A, B, d = map(int, input().split())

cord = []

for n in range(N):
    cord.append(list(map(int, input().split())))

cord[B][A] = 2

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

res = 1
count = 0
while True:
    # 왼쪽으로 90도 회전
    next_d = d - 1
    count += 1
    if next_d < 0:
        next_d = 3   
    # 회전 후 위치
    next_x = B + dx[next_d]
    next_y = A + dy[next_d]
    if cord[next_x][next_y] == 0:
        cord[next_x][next_y] = 2
        B = next_x
        A = next_y
        d = next_d
        res += 1
        count = 0
        continue
    
    d = next_d
    
    if count == 4:
        next_x = B - dx[d]
        next_y = A - dy[d]
        if cord[next_x][next_y] == 2:
            B = next_x
            A = next_y
            count = 0
        else:
            break

print(res)