def solution(schedules, timelogs, startday):
    answer = 0
    
    # 1: 월 , 2: 화 , 3: 수 , 4: 목 , 5: 금 , 6: 토 , 7: 일 -> % 7 (나머지 6, 7 제외)
    for i in range(len(schedules)):
        hope = schedules[i]
        logs = timelogs[i]
        start = startday
        flag = False
        
        # 희망 시각, 제한 시각 
        ht, hm = hope // 100, hope % 100
        lt, lm = 0, 0
        
        if hm + 10 >= 60:
            lt = hope // 100 + 1
            lm = (hope % 100 + 10) % 60
        else:
            lt = hope // 100
            lm = hope % 100 + 10
              
        for l in logs:
            # 주말이라면
            if start % 7 in (6, 0):
                start += 1
                continue
                
            at, am = l // 100, l % 100
            
            if lt < at:
                flag = True
                break
            elif lt == at and lm < am:
                flag = True
                break
            else:
                start += 1
            
        if not flag:
            answer += 1
    
    return answer