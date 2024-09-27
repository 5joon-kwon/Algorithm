N = int(input())
res = N
dic = {}
for _ in range(N):
    text = input()
    dic[text] = len(text)

sorted_key = dict(sorted(dic.items(), key = lambda x: x[0]))
sorted_dict = dict(sorted(sorted_key.items(), key = lambda x: x[1]))

for key, value in sorted_dict.items():
    print(key)