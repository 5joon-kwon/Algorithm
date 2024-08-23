n = int(input())
str = input()

A = 0
B = 0

for i in str:
    if i == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')