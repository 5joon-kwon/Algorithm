def solution(friends, gifts):
    answer = 0
    n = len(friends)
    give = {}
    get = {}
    nm = {}
    people = {}
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    
    for idx, f in enumerate(friends):
        give[f] = 0
        get[f] = 0
        nm[f] = 0
        people[f] = idx + 1

    for idx, g in enumerate(gifts):
        # 선물 준 친구, 선물 받은 친구
        i, j = g.split()
        give[i] += 1
        get[j] += 1
        arr[people[i]][people[j]] += 1
    
    # 선물 지수 : 준 선물 수 - 받은 선물 수
    score = {}
    for p in give.keys():
        score[p] = give[p] - get[p]
    
    # 선물 주고받는 사람 조합
    for give_p in give.keys():
        for get_p in give.keys():
            # 동일 인물 제외
            if give_p == get_p:
                continue
            
            # 이미 조합 봤으면 다음
            if visited[people[give_p]][people[get_p]] == 1 or visited[people[get_p]][people[give_p]] == 1:
                continue
                
            # 두 사람 중 많이 선물 준 사람이 다음 달에 선물 하나 받음
            if arr[people[give_p]][people[get_p]] > arr[people[get_p]][people[give_p]]:
                nm[give_p] += 1
                visited[people[give_p]][people[get_p]] = 1
                visited[people[get_p]][people[give_p]] = 1
            elif arr[people[give_p]][people[get_p]] < arr[people[get_p]][people[give_p]]:
                nm[get_p] += 1
                visited[people[give_p]][people[get_p]] = 1
                visited[people[get_p]][people[give_p]] = 1
            
            # 선물 주고받은 기록 없거나, 같은 수를 주고받았으면 선물지수 큰 사람이 작은 사람에게 선물 받음
            else:
                if score[give_p] > score[get_p]:
                    nm[give_p] += 1
                    visited[people[give_p]][people[get_p]] = 1
                    visited[people[get_p]][people[give_p]] = 1
                elif score[give_p] < score[get_p]:
                    nm[get_p] += 1
                    visited[people[give_p]][people[get_p]] = 1
                    visited[people[get_p]][people[give_p]] = 1
                # 선물 지수도 같다면 서로 주고받지 않음
                else:
                    visited[people[give_p]][people[get_p]] = 1
                    visited[people[get_p]][people[give_p]] = 1
                    continue

    res = []
    for v in nm.values():
        res.append(v)
    res.sort(reverse=True)
    answer = res[0]
    
    return answer