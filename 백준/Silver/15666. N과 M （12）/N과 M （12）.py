N, M = map(int, input().split())
li = list(set(map(int, input().split())))
li.sort()

res = []

def dfs(depth):
    if depth == M:
        print(*res)
        return
    
    for i in range(len(li)):
        if len(res) != 0 and res[-1] > li[i]:
            continue 
                 
        res.append(li[i])
        dfs(depth + 1)
        res.pop()

dfs(0)