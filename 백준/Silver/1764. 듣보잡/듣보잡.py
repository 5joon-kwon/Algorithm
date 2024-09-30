# import sys

# N, M = map(int, sys.stdin.readlin().strip().split())
N, M = map(int, input().split())

never = {}

for _ in range(N):
  # never[sys.stdin.readline().strip()] = 0
    never[input()] = 0
    
for _ in range(M):
  # name = sys.stdin.readline().strip()
    name = input()
    if name in never:
        never[name] += 1
    else:
        never[name] = 0

# lambda로 간단하게 표현
# li = list(filter(lambda key: never[key] == 1, never.keys()))

li = []

for key, value in never.items():
    if value == 1:
        li.append(key)

res = sorted(li)

print(len(res))
for i in res:
    print(i)
