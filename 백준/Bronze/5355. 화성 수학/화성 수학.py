case = int(input())

for _ in range(case):
    li = input().split()
    num = float(li[0])
    for i in range(len(li[1:])):
        if li[i+1] == '@':
            num *= 3
        elif li[i+1] == '%':
            num += 5
        else:
            num -= 7
    
    print(f'{num:.2f}')