import sys

N = int(input())
name_list = [sys.stdin.readline().strip() for _ in range(N)]

cnt = 0

for i in range(N):
    for j in range(i + 1, N):
        name_min = min(len(name_list[i]), len(name_list[j]))
        for k in range(1, name_min + 1):
            # 접두사 == 접미사 or 접미사 == 접두사
            if name_list[i][:k] == name_list[j][-k:] or name_list[j][:k] == name_list[i][-k:]:
                cnt += 1
                # 한 문자라도 겹치면 더이상 비교하지 않아도 됨
                break

print(cnt)