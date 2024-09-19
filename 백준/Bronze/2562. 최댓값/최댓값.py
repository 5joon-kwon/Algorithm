li = []

for _ in range(9):
    li.append(int(input()))

index = 0
ma = 0

for idx, num in enumerate(li):
    if num > ma:
        ma = num
        index = idx
        
print(ma)
print(index + 1)


# li = []
# for _ in range(9):
#    li.append(int(input())
# 
# print(max(li))
# print(li.index(max(li) + 1))
