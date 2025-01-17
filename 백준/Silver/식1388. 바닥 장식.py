N, M = map(int, input().split())

wood = []
for _ in range(N):
    wood.append(list(input()))

count = 0

# '-' 나무 판자
def vertical(tile):
    global count
    for row in wood:
        start = ''
        for i in row:
            if i == '-':
                if i != start:
                    count += 1
            start = i

# '|' 나무 판자
def horizontal(N, M, tile):
    global count
    for i in range(M):
        start = ''
        for j in range(N):
            if tile[j][i] == '|':
                if tile[j][i] != start:
                    count += 1
            start = tile[j][i]

vertical(wood)
horizontal(N, M, wood)

print(count)