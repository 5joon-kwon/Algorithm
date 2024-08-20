T = int(input())

for _ in range(T):
    N = int(input())
    max_name = ''
    max_alco = 0
    for _ in range(N):
        name, alco = input().split()
        if int(max_alco) < int(alco):
            max_name = name
            max_alco = alco
    print(max_name)