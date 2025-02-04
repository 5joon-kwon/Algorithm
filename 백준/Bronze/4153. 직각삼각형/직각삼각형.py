while True:
    li = list(map(int, input().split()))
    if sum(li) == 0:
        break
    
    max_len = max(li)
    li.remove(max_len)
    
    a, b = li[0], li[1]
    
    if max_len**2 == a**2 + b**2:
        print('right')
    else:
        print('wrong')