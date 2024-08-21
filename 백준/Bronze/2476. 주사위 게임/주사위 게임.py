N = int(input())
res = 0

for _ in range(N):
    a, b, c = map(int, input().split())
    if a == b == c:
        tot = a * 1000 + 10000
    elif a == b:
        tot = a * 100 + 1000
    elif b == c:
        tot = b * 100 + 1000
    elif c == a:
        tot = c * 100 + 1000
    else:
        tot = max(a, b, c) * 100
        
    res = max(res, tot)
    
print(res)