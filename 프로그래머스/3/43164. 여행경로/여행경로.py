from collections import defaultdict

def dfs(start, path, plane, n):
    if len(path) > n:
        return path
    
    if start not in plane:
        return
    
    for i, next_start in enumerate(plane[start]):
        if next_start is None:
            continue
        
        plane[start][i] = None
        res = dfs(next_start, path + [next_start], plane, n)
        plane[start][i] = next_start
        
        if res:
            return res
    
    return
        
def solution(tickets):
    plane = defaultdict(list)
    
    for fr, to in tickets:
        plane[fr].append(to)
    
    for key in plane.keys():
        plane[key].sort()
    
    route = dfs('ICN', ['ICN'], plane, len(tickets))
    
    return route