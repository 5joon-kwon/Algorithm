N = int(input())
M = N

i = 2
res = []
tot = 1

while True:
    if M % i == 0:
        M //= i
        tot *= i
        res.append(i)
    else:
        i += 1
    
    if tot == N:
        break
    
for r in res:
    print(r)