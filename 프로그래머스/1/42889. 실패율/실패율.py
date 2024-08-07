def solution(N, stages):
    rate = []
    for i in range(N):
        rate.append(stages.count(i+1))
    
    fail_rate = []
    stage_tot = len(stages)
    for i in range(len(rate)): 
        if stage_tot == 0:
            fail_rate.append([i+1, 0])
        else:
            fail = rate[i] / stage_tot
            fail_rate.append([i+1,fail])
        stage_tot -= rate[i]   
    
    sort_rate = sorted(fail_rate, key = lambda x : x[1], reverse = True)
    
    answer = []
    for i in sort_rate:
        answer.append(i[0])
        
    return answer