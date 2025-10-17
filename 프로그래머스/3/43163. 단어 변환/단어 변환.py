from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        pre, step = q.popleft()
        
        if pre == target:
            return step
        
        for word in words:
            if word not in visited:
                count = 0
                for i in range(len(pre)):
                    if word[i] != pre[i]:
                        count += 1

                if count == 1:
                    q.append((word, step + 1))
                    visited.add(word)