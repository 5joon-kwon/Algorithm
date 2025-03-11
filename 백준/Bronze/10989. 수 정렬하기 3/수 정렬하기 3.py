import sys
input = sys.stdin.readline

N = int(input())

cnt = [0] * 10001

for _ in range(N):
    n = int(input())
    cnt[n] += 1

for i in range(10001):
    for _ in range(cnt[i]):
        print(i)
