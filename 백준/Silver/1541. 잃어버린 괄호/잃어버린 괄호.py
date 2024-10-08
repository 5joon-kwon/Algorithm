T = input().split('-')

for i in range(len(T)):
    if '+' in T[i]:
        T[i] = T[i].split('+')  

li = []

for i in range(len(T)):
    if type(T[i]) == str:
        li.append(int(T[i]))
    else:
        s = 0
        for j in T[i]:
            s += int(j)
        li.append(s)
        
res = li[0]
for i in li[1:]:
    res -= i
    
print(res)