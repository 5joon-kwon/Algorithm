chang = 100
sang = 100

n = int(input())

for _ in range(n):
    c, s = map(int, input().split())
    if c > s:
        sang -= c
    elif c < s:
        chang -= s

print(f'{chang}\n{sang}')    