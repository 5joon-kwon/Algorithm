# import sys
# sys.stdin = open('test.txt', 'r')

word = input().upper()
alp = {}
for i in range(len(word)):
    if word[i] not in alp:
        alp[word[i]] = 1
    else:
        alp[word[i]] += 1

m = max(alp.values())
count = 0
mk = None
for k, v in alp.items():
    if m == v:
        count += 1
        mk = k

if count == 1:
    print(mk)
else:
    print('?')