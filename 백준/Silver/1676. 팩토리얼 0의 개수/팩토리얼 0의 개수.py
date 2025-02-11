N = int(input())

res = 1
for i in range(1, N + 1):
    res *= i
    
str_res = str(res)
li = []

for i in range(1, len(str_res) + 1):
    if str_res[-i] != '0':
        break
    else:
        li.append(str_res[-i])

print(len(li))