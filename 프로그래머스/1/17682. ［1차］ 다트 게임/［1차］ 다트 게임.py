def solution(dartResult):
    score = []
    bonus = []
    option = []
    idx = 0
    
    for i in range(len(dartResult)):
        if dartResult[i] == "S" or dartResult[i] == 'D' or dartResult[i] == 'T':
            score.append(dartResult[idx:i])
            bonus.append(dartResult[i])
            idx = i + 1
            if i == len(dartResult) - 1:
                option.append('None')
                break
            elif dartResult[i+1] == '*' or dartResult[i+1] == '#':
                option.append(dartResult[i+1])
                idx = i + 2
            else:
                option.append('None')      
        
    sc = [0, 0, 0]
    
    for i in range(3):
        if bonus[i] == 'S':
            sc[i] += int(score[i])
        elif bonus[i] == 'D':
            sc[i] += int(score[i]) ** 2
        else:
            sc[i] += int(score[i]) ** 3
            
        if option[i] == '*':
            if i == 0:
                sc[i] *= 2
            else:
                sc[i] *= 2
                sc[i - 1] *= 2
                
        elif option[i] == '#':
            sc[i] *= (-1)    
            
    total = sc[0] + sc[1] + sc[2]
    return total