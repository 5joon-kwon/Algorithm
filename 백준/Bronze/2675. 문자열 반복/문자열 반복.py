case = int(input())

for _ in range(case):
    S, R = input().split()
    out = ''
    for i in range(len(R)):
        out += R[i] * int(S)
    print(out)