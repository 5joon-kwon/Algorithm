import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

def find_():
    home = []
    chicken = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                home.append((i, j))
            elif city[i][j] == 2:
                chicken.append((i, j))
    
    return home, chicken

# 도시의 치킨 거리
def cal():
    tot = 0
    for hi, hj in home:
        min_d = float('inf')
        for ci, cj in li:
            min_d = min(min_d, abs(hi - ci) + abs(hj - cj))
        tot += min_d
    return tot

# 치킨집 M개 고르기 (조합)
def dfs(start):
    global min_dist

    # M개 고르면 도시의 치킨 거리 구하기
    if len(li) == m:
        min_dist = min(min_dist, cal())
        return
    
    for i in range(start, len(chicken)):
        li.append(chicken[i])
        dfs(i + 1)
        li.pop()

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

home, chicken = find_()
min_dist = float('inf')
li = []

dfs(0)
print(min_dist)
