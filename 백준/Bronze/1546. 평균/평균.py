N = int(input())
li = list(map(int, input().split()))

M = max(li)

new = []
for i in range(N):
    new.append(li[i] / M * 100)

result = sum(new) / N
print(result)