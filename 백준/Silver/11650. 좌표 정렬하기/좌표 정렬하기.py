N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

li_sorted = sorted(li, key = lambda x: (x[0], x[1]))

for i in li_sorted:
    print(str(i[0]) + ' ' + str(i[1]))