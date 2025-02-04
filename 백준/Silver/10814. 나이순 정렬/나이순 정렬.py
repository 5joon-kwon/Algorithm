N = int(input())
li = []

for i in range(N):
    a, b = input().split()
    li.append((i, int(a), b))

li_age = sorted(li, key = lambda x: (x[1], x[0]))

for i in li_age:
    print(i[1], i[2])