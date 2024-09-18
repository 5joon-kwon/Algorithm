a, b = map(int, input().split())

if a > b:
    a, b = b, a

one_to_b = (b * (b + 1)) // 2
one_to_a = ((a - 1) * a) // 2
res = one_to_b - one_to_a

print(res)