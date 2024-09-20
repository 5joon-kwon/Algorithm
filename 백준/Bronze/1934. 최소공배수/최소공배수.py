num = int(input())

def GCD(a, b):
    if a < b:
        a, b = b, a
    
    while b > 0:
        a, b = b, a % b
        
    return a

for _ in range(num):
    a, b = map(int, input().split())
    res = (a * b) // GCD(a, b)
    print(res)