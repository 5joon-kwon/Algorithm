N = int(input())
shirt = list(map(int, input().split()))
T, P = map(int, input().split())

order = 0

for s in shirt:
    if s == 0:
        continue
    
    if s // T > 0:
        if s % T > 0:
            order += (s // T) + 1
        else:
            order += s // T
    else:
        order += 1

print(order)
print(N // P, N % P)