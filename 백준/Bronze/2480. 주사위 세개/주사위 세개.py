a, b, c = map(int, input().split())
max = a

if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
elif c == a:
    print(1000 + c * 100)
else:
    if max < b:
        max = b
    if max < c:
        max = c
    print(max * 100)