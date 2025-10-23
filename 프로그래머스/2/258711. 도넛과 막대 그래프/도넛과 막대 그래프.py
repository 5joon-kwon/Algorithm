def solution(edges):
    max_node = 0
    for i, o in edges:
        max_node = max(max_node, i, o)
    
    in_deg = [0] * (max_node + 1)
    out_deg = [0] * (max_node + 1)
    
    for fro, to in edges:
        out_deg[fro] += 1
        in_deg[to] += 1
    
    gen_node = -1
    stick = eight = 0
    
    for i in range(1, max_node + 1):
        if in_deg[i] == 0 and out_deg[i] >= 2:
            gen_node = i
        elif in_deg[i] > 0 and out_deg[i] == 0:
            stick += 1
        elif in_deg[i] >= 2 and out_deg[i] == 2:
            eight += 1
        
    donut = out_deg[gen_node] - stick - eight

    return [gen_node, donut, stick, eight] 