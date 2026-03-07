import sys
input = sys.stdin.readline

n = int(input())
weights = {}

for _ in range(n):
    word = input().strip()
    length = len(word)

    for i in range(length):
        ch = word[i]
        value = 10 ** (length - i - 1)
        weights[ch] = weights.get(ch, 0) + value

values = sorted(weights.values(), reverse=True)

digit = 9
answer = 0

for v in values:
    answer += v * digit
    digit -= 1

print(answer)