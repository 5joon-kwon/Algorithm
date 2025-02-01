N = int(input())

num = 666
count = 0
initial = 666

while count != N:  
    if str(num) in str(initial):
        count += 1
        initial += 1
    else:
        initial += 1

print(initial - 1)