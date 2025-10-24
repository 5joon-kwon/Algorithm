from collections import defaultdict

def solution(id_list, report, k):
    users = defaultdict(set)
    sued = defaultdict(int)
    for r in report:
        f, t = r.split(' ')
        if t in users[f]:
            continue
        else:
            users[f].add(t)
            sued[t] += 1
    
    lock = []
    for user in sued.keys():
        if  sued[user] >= k:
            lock.append(user)
    
    answer = defaultdict(int)
    for i in id_list:
        answer[i] = 0
        
    for user in lock:
        for i in id_list:
            if user in users[i]:
                answer[i] += 1

    return [v for v in answer.values()]