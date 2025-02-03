N = int(input())

def vinyl(n):
    if n == 4:
        return -1
    
    if n % 5 == 0:
        return n // 5

    count_5 = n // 5
    sugar = n % 5

    if sugar % 3 == 0:
        return count_5 + sugar // 3
    else:
        while True:
            count_5 -= 1
            sugar += 5
            
            if sugar % 3 == 0:
                return count_5 + sugar // 3

            if count_5 == 0:
                return -1

print(vinyl(N))