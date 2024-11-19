cord = input()
low = int(cord[1])
col = cord[0]

low_list = [1, 2, 3, 4, 5, 6, 7, 8]
col_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = col_list.index(col)
y = low_list.index(low)
res = 0

# 1. 수평으로 두칸 이동한 뒤에 수직으로 한 칸 이동하기
if x - 2 >= 0 and y - 1 >= 0:
    res += 1
if x - 2 >= 0 and y + 1 <= 7:
    res += 1
if x + 2 <= 7 and y - 1 >= 0:
    res += 1
if x + 2 <= 7 and y + 1 <= 7:
    res += 1

# 2. 수직으로 두칸 이동한 뒤에 수평으로 한 칸 이동하기
if y - 2 >= 0 and x - 1 >= 0:
    res += 1
if y - 2 >= 0 and x + 1 <= 7:
    res += 1
if y + 2 <= 7 and x - 1 >= 0:
    res += 1
if y + 2 <= 7 and x + 1 <= 7:
    res += 1

print(res)