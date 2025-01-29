sset = set()

for _ in range(10):
    n = int(input())
    sset.add(n % 42)

print(len(sset))