N = int(input())
li = list(map(int, input().split()))
count = 0

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    return True

for x in li:
    if is_prime(x):
        count += 1

print(count)