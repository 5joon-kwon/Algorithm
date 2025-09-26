from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, Q = map(int, input().split())
arr = [[2] * (N + 2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N + 2)]
war = [[0, 0, 0, 0, 0]] + [list(map(int, input().split())) for _ in range(M)]
order = [list(map(int, input().split())) for _ in range(Q)]
init_k = [0]
wmap = [[0] * (N + 2) for _ in range(N + 2)]

for idx, w in enumerate(war[1:]):
    init_k += [w[4]]
    for i in range(w[0], w[0] + w[2]):
        wmap[i][w[1]:w[1] + w[3]] = [idx + 1] * w[3]

def push_war(sidx, dr):
    q = deque()
    pset = set()
    damage = [0] * (M + 1)
    
    q.append(sidx)
    pset.add(sidx)
    
    while q:
        widx = q.popleft()
        wi, wj, wh, ww, wk = war[widx]
        
        ni, nj = wi + di[dr], wj + dj[dr]
        for i in range(ni, ni + wh):
            for j in range(nj, nj + ww):
                if arr[i][j] == 2:
                    return
        
                if arr[i][j] == 1:
                    damage[widx] += 1
    
        for idx in range(1, M + 1):
            if idx in pset or war[idx] is None:
                continue

            ti, tj, th, tw, tk = war[idx]
            
            # if ni > ti + th - 1 or ni + wh - 1 < ti or nj > tj + tm - 1 or nj + wm - 1 < tj:
            #     continue
            
            if ni <= ti + th - 1 and nj <= tj + tw - 1 and ni + wh - 1 >= ti and nj + ww - 1 >= tj:
                q.append(idx)
                pset.add(idx)

    damage[sidx] = 0
    
    ### 디버그용 ##########################
    for idx in pset:
        if war[idx] is None:
            continue
        
        ci, cj, ch, cw, ck = war[idx]
        for i in range(ci, ci + ch):
            wmap[i][cj:cj + cw] = [0] * cw
    #####################################
    
    for idx in pset:
        if war[idx] is None:
            continue
        
        ci, cj, ch, cw, ck = war[idx]
        if ck - damage[idx] <= 0:
            war[idx] = None
        else:
            ni, nj = ci + di[dr], cj + dj[dr]   
            war[idx] = [ni, nj, ch, cw, ck - damage[idx]]
            
            ### 디버그용 ##########################
            for i in range(ni, ni + ch):
                wmap[i][nj:nj + cw] = [idx] * cw
            #####################################        

for _ in range(Q):
    idx, dr = order.pop(0)
    if war[idx] is not None:
        push_war(idx, dr)
    
ans = 0
for idx in range(1, M + 1):
    if war[idx] is None:
        continue
    ans += init_k[idx] - war[idx][4]
    
print(ans)