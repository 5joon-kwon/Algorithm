def solution(today, terms, privacies):
    terms_list = []
    privacies_list = []
    answer = []
    
    for i in terms:
        terms_list.append(i.split(' '))
    
    for i in privacies:
        privacies_list.append(i.split( ))
    
    if(today[5] == '0'):
        t_month = int(today[6])
    else:
        t_month = int(today[5:7])
    
    t_year = int(today[:4])

    if(today[8] == '0'):
        t_day = int(today[9])
    else:
        t_day = int(today[8:10])
                
    for idx, i in enumerate(privacies_list):
        for j in terms_list:
            year = int(i[0][:4])
            
            if(len(i[0][5]) == '0'):
                month = int(i[0][6])
            else:
                month = int(i[0][5:7])
            
            if(len(i[0][8]) == '0'):
                month = int(i[0][9])
            else:
                day = int(i[0][8:10])
            
            if i[1] == j[0]:
                day -= 1
                if(day == 0):
                    day = 28
                    month -= 1
                if(month == 0):
                    month = 12
                    year -= 1 
                
                m = int(j[1]) % 12
                mm = int(j[1]) // 12
                    
                month += m
                year += mm
                if(month > 12):
                    year += 1
                    month -= 12
                
                if(year < t_year and (idx+1 not in answer)):
                    answer.append(idx+1)
                elif(year == t_year and month < t_month and (idx+1 not in answer)):
                    answer.append(idx+1)
                elif(year == t_year and month == t_month and day < t_day and (idx+1 not in answer)):
                    answer.append(idx+1)
               
    return answer