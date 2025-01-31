N, M = map(int, input().split())

chess = []
count = 0

for _ in range(N):
    chess.append((input()))

width = N - 7
height = M - 7
test = [[0] * height for _ in range(width)]

case1 = ['BWBWBWBW', 
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB']

case2 = ['WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW',
         'WBWBWBWB',
         'BWBWBWBW']

def differ(graph):
    cnt1 = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if graph[i][j] != case1[i][j]:
                cnt1 += 1

    for i in range(8):
        for j in range(8):
            if graph[i][j] != case2[i][j]:
                cnt2 += 1

    return min(cnt1, cnt2)

for i in range(width):
    for j in range(height):
        t = []
        for k in range(i, i + 8):
            t.append(chess[k][j:j+8])
        test[i][j] = differ(t)

minn = 999
for m in test:
    if minn > min(m):
        minn = min(m)
        
print(minn)