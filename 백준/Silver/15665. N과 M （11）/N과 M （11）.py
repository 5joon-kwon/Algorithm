import sys
input = sys.stdin.readline
N, M = map(int,input().split())
LIST = sorted(list(set(map(int,input().split()))))

total = []

def back():
    if len(total) == M:
        print(*total)
        return 
    
    for i in range(len(LIST)):
        total.append(LIST[i])
        back()
        total.pop()

back()