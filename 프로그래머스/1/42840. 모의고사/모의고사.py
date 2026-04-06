def solution(answers):
    first = [1,2,3,4,5] * 2000
    second = [2,1,2,3,2,4,2,5] * 1250
    third = [3,3,1,1,2,2,4,4,5,5] * 1000
    supo = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        # if first[i % len(first)] == answer[i]
        if first[i] == answers[i]:
            supo[1] += 1
        
        # if second[i % len(second)] == answer[i]
        if second[i] == answers[i]:
            supo[2] += 1
        
        # if third[i % len(third)] == answer[i]
        if third[i] == answers[i]:
            supo[3] += 1
    
    ans = []
    maxi = max(supo.values())
    for k, v in supo.items():
        if maxi == v:
            ans.append(k)

    return ans