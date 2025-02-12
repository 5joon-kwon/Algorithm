N = int(input())
person = [list(map(int, input().split())) for _ in range(N)]

score = []

for i in range(N):
    grade = 1
    for j in range(N):
        if i == j:
            continue
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            grade += 1
    score.append(grade)

print(*score)
