def solution(today, terms, privacies):
    ty, tm, td = map(int, today.split('.'))
    kinds = {}
    for term in terms:
        k, t = term.split()
        kinds[k] = int(t)
    
    li = []
    for idx, p in enumerate(privacies):
        date, k = p.split()
        y, m, d = map(int, date.split('.'))
        li.append([idx + 1, y, m, d, k])
    
    answer = []
    # 한달 : 28일
    # 수집날도 하루로 인정 21/01/05 - 22/01/04
    for i in li:
        num, y, m, d, k = i
        
        # nyear, nmonth
        sum_month = m + kinds[k]
        if sum_month > 12:
            if sum_month % 12 == 0:
                ny = y + (sum_month // 12) - 1
                nm = 12
            else:
                ny = y + (sum_month // 12)
                nm = sum_month % 12
        else:
            ny = y
            nm = sum_month
        
        # nday
        if d == 1:
            if nm == 1:
                ny -= 1
                nm = 12
                nd = 28
            else:
                nm -= 1
                nd = 28
        else:
            nd = d - 1
        
        # nyear < tyear : append
        if ny < ty:
            answer.append(num)
            continue
        # nmonth < tmonth : append
        elif ny == ty and nm < tm:
            answer.append(num)
            continue
        # nday < tday : append
        elif ny == ty and nm == tm and nd < td:
            answer.append(num)
            continue
    
    answer.sort()
    return answer