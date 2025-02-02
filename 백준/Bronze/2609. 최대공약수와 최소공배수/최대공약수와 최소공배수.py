x, y = map(int, input().split())

if x < y:
    x, y = y, x

def GCD(x, y):        
    while y > 0:
        x, y = y, x % y
    
    return x

print(GCD(x, y))
print((x * y) // GCD(x, y))