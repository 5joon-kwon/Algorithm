N = int(input())

li = []
v = [False] * (N + 1)

def permutation(cnt):
    if cnt == N:
        print(*li)
        return
    
    for i in range(1, N + 1):
        if v[i]:
            continue

        v[i] = True
        li.append(i)
        permutation(cnt + 1)
        li.pop()
        v[i] = False

permutation(0)