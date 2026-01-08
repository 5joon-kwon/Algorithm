l, c = map(int, input().split())
words = list(input().split())
words.sort()

mo = set(('a', 'e', 'i', 'o', 'u'))
ans = []

# 모음, 자음의 개수를 매개변수로 받기
def back(idx, m, j):    
    # 가지치기
    if len(ans) + (c - idx) < l:
        return
    
    if len(ans) == l:
        # 최소 한 개의 모음 + 최소 두 개의 자음
        if m >= 1 and j >= 2:
            print(''.join(ans))
        return
    
    for i in range(idx, c):
        ans.append(words[i])
        
        # 모음/자음에 따른 재귀
        if words[i] in mo:
            back(i + 1, m + 1, j)
        else:
            back(i + 1, m, j + 1)
            
        ans.pop()

back(0, 0, 0)