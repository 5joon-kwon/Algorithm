def solution(new_id):
    lower_id = new_id.lower()
    elim = ""
    
    for i in lower_id:
        if((i.isalpha() != True and i.isdigit() != True) and i not in ['-', '_', '.']):
            i = ''
            elim += i
        else:
            elim += i      
            
    while(".." in elim):
        elim = elim.replace("..", ".")        

    elim_id = elim.strip('.')
    
    if(elim_id == ''):
        elim_id += 'a'
    
    if(len(elim_id) > 15):
        elim_id = elim_id[:15]
        elim_id = elim_id.strip('.')
    
    while(len(elim_id) < 3):
        elim_id += elim_id[-1]
            
    answer = elim_id
    
    return answer