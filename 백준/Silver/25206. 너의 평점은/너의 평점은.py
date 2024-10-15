import sys
input = sys.stdin.readline

res = 0
num = 0

for _ in range(20):
    name, score, grade = input().strip().split()
    if grade == 'A+':
        res += float(score) * 4.5
        num += float(score)
    elif grade == 'A0':
        res += float(score) * 4.0
        num += float(score)
    elif grade == 'B+':
        res += float(score) * 3.5
        num += float(score)
    elif grade == 'B0':
        res += float(score) * 3.0
        num += float(score)
    elif grade == 'C+':
        res += float(score) * 2.5
        num += float(score)
    elif grade == 'C0':
        res += float(score) * 2.0
        num += float(score)
    elif grade == 'D+':
        res += float(score) * 1.5
        num += float(score)
    elif grade == 'D0':
        res += float(score) * 1.0
        num += float(score)
    elif grade == 'F':
        res += float(score) * 0.0
        num += float(score)
    else:
        continue

print(res / num)            