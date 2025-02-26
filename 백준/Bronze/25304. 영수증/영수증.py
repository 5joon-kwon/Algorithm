X = int(input())
N = int(input())

res = 0

for _ in range(N):
    price, num = map(int, input().split())
    res += price * num

if res == X:
    print('Yes')
else:
    print('No')