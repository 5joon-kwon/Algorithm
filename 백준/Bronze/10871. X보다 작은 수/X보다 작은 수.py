N, X = map(int, input().split())
li = list(map(int, input().split()))

res = []
for i in li:
    if X > i:
        res.append(i)

print((' ').join(map(str, res)))