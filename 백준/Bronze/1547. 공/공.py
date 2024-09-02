M = int(input())
cup = [1, 0, 0]

for _ in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    cup[X], cup[Y] = cup[Y], cup[X]

for i in range(3):
    if cup[i] == 1:
        print(i + 1)
        break