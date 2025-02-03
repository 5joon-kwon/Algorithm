N = int(input())

def vinyl(n):
    # 최대한 5kg 봉지를 사용
    count_5 = n // 5
    while count_5 >= 0:
        # 5kg 봉지 사용하고 남은 설탕
        sugar = n - (5 * count_5)
        if sugar % 3 == 0:
            return count_5 + (sugar // 3)
        count_5 -= 1
    return -1

print(vinyl(N))