N = int(input())

cnt = 1
res = 1
while cnt < N:
    cnt += 6 * res
    res += 1

print(res)