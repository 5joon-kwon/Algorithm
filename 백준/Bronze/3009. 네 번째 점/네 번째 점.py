x_coord = []
y_coord = []
xy = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coord.append(x)
    y_coord.append(y)
    xy.append([x, y])
    
x_min = min(x_coord)
x_max = max(x_coord)
y_min = min(y_coord)
y_max = max(y_coord)

li = [[x_min, y_min], [x_min, y_max], [x_max, y_min], [x_max, y_max]]

for i in li:
    if i not in xy:
        print(i[0], i[1])

# 간단한 풀이 : min(list, key = list.count) 이용

x_coord = []
y_coord = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coord.append(x)
    y_coord.append(y)

x = min(x_coord, key = x_coord.count)
y = min(y_coord, key = y_coord.count)

print(x, y)
