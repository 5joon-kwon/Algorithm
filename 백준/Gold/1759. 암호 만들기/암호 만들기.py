l, c = map(int, input().split())
words = list(input().split())
words.sort()

mo = set(('a', 'e', 'i', 'o', 'u'))
ans = []

def back(idx):    
    if len(ans) == l:
        # 최소 한 개의 모음 + 최소 두 개의 자음
        # 모음 : in mo
        m, j = 0, 0
        flag = False
        for w in ans:
            if w in mo:
                m += 1
            else:
                j += 1
            
            if m >= 1 and j >= 2:
                flag = True
                break
                
        if flag:
            for w in ans:
                print(w, end='')
            print()
        
        return
    
    for i in range(idx, c):
        ans.append(words[i])
        back(i + 1)
        ans.pop()

back(0)