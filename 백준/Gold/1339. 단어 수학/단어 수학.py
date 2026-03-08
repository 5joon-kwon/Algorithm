import sys
# sys.stdin = open('test.txt', 'r')
input = sys.stdin.readline

n = int(input())

words = [input().strip() for _ in range(n)]
dic = {}

for word in words:
    length = len(word)
    for i in range(length):
        digit = 10 ** (length - i - 1)
        if word[i] in dic:
            dic[word[i]] += digit
        else:
            dic[word[i]] = digit

sdic = sorted(dic.values(), reverse=True)

num = 9
res = 0
for s in sdic:
    res += num * s
    num -= 1
print(res)