S = int(input())
sum = 0
result = 0

for i in range(1, S+1):
    sum += i
    result += 1
    if S == 1:
        print(result)
        break
    if sum > S:
        print(result - 1)
        break