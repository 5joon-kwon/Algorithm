def solution(cacheSize, cities):
    cache = []
    time = 0
    
    if cacheSize == 0:  # cacheSize가 0이면 cities 요소 모두 miss 이므로 개수 x 5(시간)
        time = len(cities) * 5
    else:
        for i in cities:
            i = i.upper()
            if i not in cache:              # cache안에 city 없는 경우
                if len(cache) < cacheSize:  # cache가 가득차지 않은 경우
                    cache.append(i)
                    time += 5               # cache miss 이므로 +5(시간)
                else:                       # cache가 가득 찬 경우
                    cache.pop(0)            # cache의 첫번째 요소가 가장 오래전에 사용: 제거
                    cache.append(i)         # 새롭게 city 추가
                    time += 5
            else:                           # cache안에 city 있는 경우
                cache.pop(cache.index(i))   # city index 위치 제거
                cache.append(i)             # 새롭게 city 추가
                time += 1

    return time