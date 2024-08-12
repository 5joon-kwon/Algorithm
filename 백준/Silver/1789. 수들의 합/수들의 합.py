S = int(input())
sum = 0
result = 0

for i in range(1, S+1):
    sum += i
    result += 1

    if sum > S:
        print(result - 1)
        break
