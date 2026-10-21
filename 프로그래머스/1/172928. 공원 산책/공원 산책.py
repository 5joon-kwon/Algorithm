def solution(park, routes):
    graph = []
    route = []
    for p in park:
        graph.append(list(p))
    for r in routes:
        op, n = r.split()
        route.append([op, n])
    N = len(graph)
    M = len(graph[0])    
    si, sj = 0, 0
    
    flag = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'S':
                si, sj = i, j
                flag = True
                break
        if flag:
            break
    
    for op, n in route:
        di, dj = 0, 0
        if op == 'N':
            di, dj = -1, 0
        elif op == 'S':
            di, dj = 1, 0
        elif op == 'W':
            di, dj = 0, -1
        else:
            di, dj = 0, 1
        
        flag2 = False
        for k in range(1, int(n) + 1):
            ni, nj = si + di * k, sj + dj * k
            if not (0 <= ni < N and 0 <= nj < M and graph[ni][nj] != 'X'):
                flag2 = True
                break
        
        if flag2:
            continue
        else:
            si, sj = ni, nj
            
            
    answer = [si, sj]
    return answer