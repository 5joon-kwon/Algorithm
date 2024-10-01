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


# 집합으로 푼 풀이
# import sys

# N, M = map(int, sys.stdin.readline().strip().split())

# set1 = set()
# set2 = set()

# # 듣도 못한 사람
# for _ in range(N):
#     set1.add(sys.stdin.readline().strip())

# # 보도 못한 사람
# for _ in range(M):
#     set2.add(sys.stdin.readline().strip())

# # 듣보잡들
# result = sorted(list(set1 & set2))

# # 듣보잡 수
# print(len(result))

# # 듣보잡 이름
# for x in result:
#     print(x)
