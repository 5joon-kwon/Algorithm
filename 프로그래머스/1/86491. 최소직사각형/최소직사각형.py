def solution(sizes):
    long, short = [], []
    
    for w, h in sizes:
        if w > h:
            long.append(w)
            short.append(h)
        else:
            long.append(h)
            short.append(w)
    
    # print(max(long), max(short))

    return max(long) * max(short)