def solution(survey, choices):
    personal = [0,0,0,0,0,0,0,0]
    for i, j in zip(survey, choices):
        if i == "RT":
            if j < 4:
                personal[0] += 4 - j
            elif j > 4:
                personal[1] += j - 4
                
        elif i == "TR":
            if j < 4:
                personal[1] += 4 - j
            elif j > 4:
                personal[0] += j - 4
            
        elif i == "CF":
            if j < 4:
                personal[2] += 4 - j
            elif j > 4:
                personal[3] += j - 4
            
        elif i == "FC":
            if j < 4:
                personal[3] += 4 - j
            elif j > 4:
                personal[2] += j - 4
                
        elif i == "JM":
            if j < 4:
                personal[4] += 4 - j
            elif j > 4:
                personal[5] += j - 4 
                
        elif i == "MJ":
            if j < 4:
                personal[5] += 4 - j
            elif j > 4:
                personal[4] += j - 4
            
        elif i == "AN":
            if j < 4:
                personal[6] += 4 - j
            elif j > 4:
                personal[7] += j - 4
            
        else:
            if j < 4:
                personal[7] += 4 - j
            elif j > 4:
                personal[6] += j - 4

    answer = ''
    
    if personal[0] >= personal[1]:
        answer += 'R'
    else:
        answer += 'T'   
    
    if personal[2] >= personal[3]:
        answer += 'C'
    else:
        answer += 'F'  
        
    if personal[4] >= personal[5]:
        answer += 'J'
    else:
        answer += 'M'  
        
    if personal[6] >= personal[7]:
        answer += 'A'
    else:
        answer += 'N'          
    
    return answer